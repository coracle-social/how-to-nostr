Thus far we've focused mostly on Nostr as data in terms of data modeling, signatures, and identity, but that's really only half of the story. Nostr is an alternative to decentralized peer-to-peer protocols which attempt to repurpose the architecture of the internet to facilitate direct communication between peers.

Peer-to-peer technology is really neat, but it's also hard to get right because it works against the grain of the internet as it has been used for the last 30 years. Things like NAT traversal for managing incoming connections behind a firewall make this especially difficult.

Now that's not to say we should completely ignore P2P technologies at all. Things like Meshtastic, which is internet over radio, and peer-to-peer Bluetooth connections or NFC connections are all really interesting techniques that can be applied in parallel with a more traditional internet architecture.

Nostr attempts to get many of the benefits of peer-to-peer style architectures without a lot of the hassle. And the basic way that this is done is using WebSocket servers. WebSocket servers have all the same problems that regular servers have in terms of being gatekept by internet service providers, as well as TLS certificates and DNS registrars, depending on how conventional you want to set them up. DNS can be bypassed, but then users have to deal with IP addresses. TLS can be bypassed, but then implementations have to run things through Tor, which is feasible in some locations, but not on web applications.

The baseline for relays is conventional TLS with conventional domain names. And in true Nostr fashion, this is "good enough."™

Because anyone can buy a domain name and spin up a server, there are hundreds of relays out there that can be used for storing signed data.

A key part of using Nostr is reliance on more than one relay for storing your data. As we mentioned in the previous chapter, relays can't falsify anything because your data is signed. They don't have the ability to lock users in or to create a data moat. What they do have the ability to do though is to censor or delete user data.

If you use only a single relay, that relay has complete control over which of your signed notes, signed events, get rebroadcast to other people. And it may even selectively censor data, depending on who's asking for it or what you're publishing. Adding an additional relay decreases your vulnerability to censorship by a massive amount. Adding a third relay increases it even further. If, say, you have a 10% chance all things being equal of being deplatformed by a single relay, having two relays gives you a 1% chance. Having three relays gives you a 0.1% chance of being deplatformed.

And so you really need very few relays in order to get many of the benefits. This also means that there are diminishing returns to adding more relays. Some people add 20, 30 different relays to their relay selections on Nostr and all that does is multiply the amount of bandwidth that's burned when sending and receiving messages. A good number of relays to choose for inbox, outbox, or private DM relays is three to five. That gives you plenty of redundancy without clogging things up too much.

In one of Rich Hickey's talks, "Simple Made Easy," he mentions the distinction between easy and simple. Easy means something is close at hand. It's convenient. It may not be the best solution, but it's accessible. Simple means that something does one thing well without being complicated by different concerns. Relays are not really simple. Relays are easy. Relays use WebSockets which are a layer on top of HTTP which is a layer on top of TCP/IP, which is itself a fairly complicated protocol.

The trade-off here is that the technology, again, is not ideal, but good enough. WebSocket servers also allow for duplex communication rather than request-response, which allows servers to push new information to the client as soon as they receive it.

Using WebSockets doesn't preclude the use of other transport protocols to send events between peers. I'm not talking about Nostr over HTTP. HTTP, while simple and more familiar for developers who are used to working with web technologies, is strictly worse than using WebSockets because HTTP doesn't allow for server-sent events, increases latency through polling, and makes clients and relays less efficient.

What I am referring to is alternative transport protocols that have a different trade-off balance from WebSockets. So in theory you could come up with a binary encoding of Nostr events and send them over QUIC, which would eliminate a lot of the overhead. That would be useful for high performance applications and servers.

Alternatively, you might put a bunch of Nostr events in a JSONL file and store them on IPFS. These events would then be replicated on a different decentralized network and could be downloaded by a client supporting that transport.

Another example would be to use P2P technologies like Iroh or Pear as a way of adding connectivity via progressive enhancement. Which is a way of enhancing the connectivity of Nostr without breaking the base protocol. So this might be useful on a mobile app, which doesn't always have internet connectivity in order to reach relays, like somewhere in rural Africa, but where it can gossip with other people's phones when it is in proximity to them.

In this case, the phones wouldn't exactly act like relays. In this case the client would essentially be a relay, although it wouldn't be a WebSocket server.

These alternative transport protocols have by and large not been specified or implemented, but there's nothing to keep us from creating them.

This technique was pioneered originally by Scuttlebutt, which started with the P2P technologies and then added pubs as a way of bridging devices that weren't directly connected. Nostr simply reverses this model and makes pubs first and P2P the progressive enhancement.

That's enough theory for now. Let's get into what relays actually look like, assuming a WebSocket context.

Relays are, in the simplest terms, repositories of events. They hold a bunch of events in some database or other and grant access to those events using the Nostr WebSocket protocol. This protocol involves sending JSON-encoded messages over WebSockets using a few different verbs. The main ones being, in all caps, EVENT, which allows clients to send an event to a relay; OK, which allows relays to respond to that event publish with success or failure and an error message; and on the read side, clients can send a REQ and receive one or more EVENT responses, which contain a JSON-encoded event.

REQ additionally takes filters which we talked about in a previous chapter, which allow clients to target the events that they want.

There are some other commands, and we'll get to two of them later: AUTH and Negentropy. But this is the essence of what a relay is: you put events into it and you take events back out. That's pretty much all you need to do. Things like COUNT might seem useful at first, but they add additional implementation burden to relays without producing any real utility. Because in order to count events in a decentralized network, you need a way to reconcile those events between multiple servers. COUNT does nothing to do that. It's only useful in a context when you're working with a single relay, which exists but is relatively rare.

Treating relays as simple event repositories allows for layering on additional functionality using separate interfaces. We'll get to this later on, but DVMs or data vending machines are a great way to do this. If you need to count events, the data vending machine can operate against one or more or a dynamic set of relays and do counting more efficiently and accurately than any relay could do on its own. The DVM protocol is completely open in the same way that Nostr events are, which means that any additional functionality can be layered on top of relays through DVMs.

For the sake of decentralization, it's my opinion that the relay interfaces should be kept as simple as possible—as minimal as possible—to reduce implementation burden and maximize interoperability.

That said, there is one additional thing that relays should be responsible for, and that's access control. Access control on Nostr is implemented by the AUTH verb. When a relay wants to know who is accessing its repository, it issues an AUTH with a challenge string. The client then signs this challenge, incorporates this challenge string into a Kind 22242 event, signs that and sends it back to the relay.

Because only, presumably only the user who holds the private key can sign such an event, the relay then knows who is accessing the relay and can respond by rejecting published events, rejecting requests, or selectively filtering data before returning it to the client.

This is useful for two distinct things: content curation and access control. Many relays have policies about what kind of content is allowed on their relay, whether based on content analysis or the social network or proof of work or when an event was published. And AUTH allows them to implement these content curation rules.

This is similar but distinct from access control. Relays may or may not have content curation policies, but they may want to allow access to the content that they store only to particular users. This can be useful for community relays.

Nostr as a network is highly partition tolerant, unlike things like Secure Scuttlebutt, which use Merkle trees to connect all events from a single key together. This means that it's impossible to download a single event without downloading all events that came before. On Nostr, you can download any set of events that you want. The cost of this, of course, is that you never know if you have all the events. But the benefit is that the same identity can present itself differently in different contexts.

You can have public microblogging notes and private microblogging notes depending on which relays are storing the content.

Noteworthy in this context is the NIP-70 protected tag, which encourages relays to reject events not signed by the person who's authenticated to the relay.

So to elaborate on my definition of a relay from earlier, a relay is a repository of events which may have policies related to content curation and access control.

The final piece of all this is Negentropy, which is a set-based reconciliation protocol created by Doug Hoyt for efficiently replicating events between two relays, or between a client and a relay. This basically works like your standard request-response, but instead of sending all events, it sends a compact representation of all event IDs that match the filters. Clients can then compare that against their local database and request any missing events.

In the past, this technique has been used to naively replicate events across the entire Nostr network. One project in particular called Blaster encouraged people to send notes to Blaster and it would forward those notes across hundreds of other relays.

This is unfortunately a short-term solution to a long-term problem and does not at all scale, but only becomes more expensive as more relays are stood up and as more data is published to the network. When you use aggressive content replication, you create hundreds of copies of each event and ask relays that you may have no relationship or alignment with to store your data for free.

This works okay when your network has a million events and 500 relays. But what about when it has a trillion events and 10,000 relays? Not every relay should store every event.

And this is where the Outbox model comes in. The Outbox model combines cryptographic identity with selective content replication.
