Thus far we've focused mostly on "Nostr as data." But data modeling, signatures, and identity are really only half of the story. Nostr is much more than a data format - what is much more interesting is its network architecture.

Many cutting-edge decentralized protocols are "peer-to-peer," which means they attempt to repurpose the architecture of the internet to facilitate direct communication between peers. Peer-to-peer technology is really neat, but it's also hard to get right because it works against the grain of the internet as it has been used for the last 30 years. Things like NAT traversal make this especially difficult.

That's not to say P2P technologies are of no use. Mesh network systems and P2P communication techniques can be great when used as fallbacks to more traditional infrastructure and networking technologies. But just like it would be very hard or impossible to completely replace the hub-and-spoke architecture of the internet with a mesh network, P2P systems are not a complete replacement for the client-server model.

Nostr attempts to get many of the benefits of P2P-style architectures without a lot of the hassle by using a pretty boring piece of web technology: WebSocket servers. WebSocket servers have all the same problems that regular servers have in terms of being gatekept by internet service providers, and relying on TLS root certificates and DNS registrars. DNS can be bypassed, but then users have to deal with IP addresses. TLS can be bypassed, but then implementations have to run things through Tor, which has its own trade-offs.

Most nostr relays use TLS with conventional domain names. And in true Nostr fashion, this is "good enough™." Because anyone can buy a domain name and spin up a server, there are hundreds of relays out there that can be used for storing signed data. If relay operators or users want to up the ante (for example if the country they live in [man-in-the-middle attacks TLS](https://en.wikipedia.org/wiki/Kazakhstan_man-in-the-middle_attack)), they can always resort to more advanced techniques. And if a particular relay goes offline, it's only one of many redundant nodes.

In "Simple Made Easy," Rich Hickey defines the distinction between easy and simple. "Easy" means something is "close at hand". Something that's easy may not be the best solution, but it's accessible. "Simple" means that something does one thing well without being complicated by different concerns. In technical terms, relays are not really simple. Relays are easy. Relays use WebSockets which are a layer on top of HTTP which is a layer on top of TCP/IP, which is itself a fairly complicated protocol.

The trade-off here is that the technology, again, is not ideal, but good enough. WebSocket servers also allow for duplex communication rather than request-response, which allows servers to push new information to the client as soon as they receive it.

Using WebSockets doesn't preclude the use of other transport protocols to send events between peers.

(As an aside, I'm not talking about Nostr over HTTP. HTTP, while simple and more familiar for developers who are used to working with web technologies, is strictly worse than using WebSockets because HTTP doesn't allow for server-sent events, increases latency through polling, and makes clients and relays less efficient. If you're going to rely on the web stack, just use WebSockets.)

What I mean rather is alternative transport protocols that have a different simplicity/ease trade-off balance from WebSockets. In theory you could come up with a binary encoding of Nostr events and send them over QUIC, which would eliminate a lot of the overhead associated with WebSockets. This might be useful for high performance applications and servers.

Alternatively, you might put a bunch of Nostr events in a JSONL file and torrent it. These events would then be replicated on a different decentralized network and could be downloaded by a client supporting that transport, improving censorship resistance (assuming the dataset is valuable enough for people to seed it).

Another example would be to use P2P technologies as progressive enhancement. In other words, you could enhance the connectivity of Nostr applications in certain scenarios without breaking the base protocol. This might be a useful when designing a mobile application for people in rural areas with little network coverage. If the network isn't available, devices would fall back to direct connection over Bluetooth or WiFi Direct.

This technique was pioneered originally by Secure Scuttlebutt (SSB), which started with P2P technologies and then added pubs as a way of bridging devices that weren't directly connected. Nostr simply reverses this model and makes pubs the primary means of communication and optionally adds P2P when required. Of course, these alternative transport protocols have by and large not been specified or implemented, but there's nothing to keep us from creating them.

In terms of transport protocol, Nostr opted for "easy" by default. But this dimension of the relay network is secondary to the network architecture itself, which adheres much more closely to Hickey's idea of "simplicity". So, setting aside the transport questions for now, let's get into what relays actually do.

# Multi-Master

A key aspect of Nostr's architecture is its reliance on more than one relay for storing data. As we mentioned in the previous chapter, relays can't falsify anything because your data is signed. They don't have the ability to lock users in or create a data moat. What they do have, however, is the ability to censor or delete user data.

If you use only a single relay, that relay has complete control over which of your signed events get rebroadcast to other people. It may even selectively censor data depending on who's asking for it or what you're publishing. Adding an additional relay decreases your vulnerability to censorship in a strightfoward way. If, say, you have a 10% chance all things being equal of being deplatformed by a single relay, publishing to two relays gives you a 1% chance; three relays gives you a 0.1% chance. Beyond that, if you're particularly sensitive to the risk of deplatforming, your best option is probably to self-host or select relays you can rely upon to host your content.

For the average user, a small number of relays can yield most of the benefits of nostr's architecture. Some people add 20 or more relays to their relay selections, but all that does is multiply the amount of bandwidth that's burned when sending and receiving messages.

The same fallacy that "more is better" is evident with relay operators - many people run a relay just so they can "run a node". But (to borrow a term from Bitcoin), you have to have "an economical node". In other words, people have to use it - and you have to keep it running.

For the average social media user, three to five popular relays is generally enough. As long as the relays provide a good mix of different admins, jurisdictions, and policies, you're very unlikely to lose all your hosts at once. Even if you do, you still have your key! Just keep a periodic backup of your content and re-broadcast it when you find more trustworthy hosts.

This ignores the problem of which relays should be used to store what content. Solving this problem is the key to making Nostr's multi-master architecture work; naive replicas result in either excessive duplication of content across all relays, or persistent failure to locate content. We'll get to that soon, but first I want to define what a relay actually is.

# Functional Relays

Relays are, in essence, repositories of events. They hold a bunch of events in some database or other and grant access to those events using the Nostr WebSocket protocol. This protocol involves sending JSON-encoded messages over WebSockets using just a few core commands:

- Clients can send an `EVENT` message in order to publish an event to a relay
- Relays respond to client `EVENT` messages with an `OK` message, which includes whether the event was accepted or rejected and an human-readable message with details
- On the read side, clients can send a `REQ` with a subscription ID and a filter
- Relays can respond by sending one or more `EVENT` messages, each of which contains an event

There are a few other control messages, including `CLOSE`, which allows a client to close a `REQ`; `CLOSED`, which allows a relay to close a `REQ`, and `EOSE`, which allows relays to let clients know when they've sent all events initially matched by a `REQ` (the relay might continue to stream matching events as it receives them).

There are some other details which we'll get to below, but this is pretty much it! A relay is just a bucket you put events into and then take them out again.

Some additional commands have been proposed, and in some cases added to the protocol, but to the extent that they stray outside of this basic repository paradigm they only complicate things for little or no benefit. One example is `COUNT`, which might seem useful at first until you consider that in order to count events in a decentralized network you need a way to reconcile those events between multiple servers. COUNT doesn't do that, making it useful only when working with a single relay.

Treating relays as simple event repositories allows for layering on additional functionality using separate interfaces. We'll get to this later on, but "data vending machines" (also known as "DVMs") are a great way to do this. If you need to count events, data vending machines allow for aggregation across multiple relays. The DVM protocol is completely open in the same way that Nostr events are, which means new functionality can easily be added, advertised, and integrated.

For the sake of decentralization, it's my opinion that the relay interfaces should be kept as minimal as possible in order to reduce implementation burden and maximize interoperability.

That said, there is one additional responsibility that relays can't really delegate: access control. Access control on Nostr is implemented by the `AUTH` verb. When a relay wants to know who opened a connection, it issues an `AUTH` message with a challenge string. The client then incorporates this challenge string into a `kind 22242` event, signs it, and sends it back to the relay.

From this point on, the relay can implement any policy it wants on the basis of the user's cryptographic identity by rejecting published events, refusing to serve requests, or selectively filtering data before returning it to the client.

This is useful for two distinct things: content curation and access control. Many relays have policies about what kind of content is allowed on their relay, whether based on content analysis, social graph analysis, proof of work, or when an event was published. Much of this data is already available on any event that gets published to a relay, but the identity of the person publishing an event can also be an important way to vet content cross-posted from elsewhere on the network, or if the user is paying to store content on the relay.

Access control is similar to, but distinct from, content curation. Relays may or may not care what events in particular they store, but they may want to allow access only to particular users. This can be useful for community relays, relays that handle direct messages, or relays that proxy content on behalf of paid subscribers.

These policies together make relays less fungible - which is, counter-intuitively, a good thing. Some large hubs accept everything except for spam, and are therefore mostly interchangeable - there's no reason to establish a relationship with one rather than the other. Other relays implement custom policies for protecting community content or direct messages, which make them more appropriate for certain use cases. Another example would be relays which return an algorithmic selection of notes from across the network, making social media "algorithms" possible.

This is an important point - to the extent that relays are treated as commodities they also have to be subsidized by businesses operating on nostr. Relays that don't have a distinctive value proposition don't have a business model. This presents the danger of leading us back into the surveillance capitalism of the existing internet. Presenting relays to the end user as distinct services providers forces users to consider who they do business with and why, creating affordances for direct monetization and alignment of incentives that wouldn't exist if relays were abstracted away.

One final thing to note in this context is [Negentropy](https://github.com/nostr-protocol/nips/blob/master/77.md), a set-based reconciliation protocol used for efficiently syncing events between two relays (or between a client and a relay). This basically works like your standard request-response, but instead of sending all events, it sends a compact representation of all event IDs that match the filters. Clients can then request any missing events.

This does a lot to facilitate content replication across relays without burning through resources, which in turn makes it possible for the network to re-organize itself to align with expections about where a given event "should" be stored.

# Replication and Routing

The Nostr network is highly partition tolerant, unlike (for example) Secure Scuttlebutt, which uses Merkle trees to connect all events from a single key together, making it impossible to download a single event without downloading all events that came before it. On Nostr, you can download any dataset you want, because events aren't tied together. The cost of this is that you never know if you have all the events; the benefit is that content can be replicated more intelligently across the network.

This is actually how Twitter's architecture works - in order to scale, they maintain a network of interrelated caching nodes. When the average user posts content it normally gets sent immediately to read caches for all of their followers. But when a very popular account posts content, it's replicated to special "famous person" caches, distributing load without excessive duplication. Their system is also overprovisioned and able to respond to dynamic load, since news events may happen without warning.

This is of course an over-simplified view of Twitter's [architecture](https://blog.x.com/engineering/en_us/topics/infrastructure/2017/the-infrastructure-behind-twitter-scale), but you can see how nostr relays might correspond to cache nodes. If Nostr is to scale, it must adopt a similar architecture. This requires not only the availability of enough nodes to support the network, but (arguably more importantly) heuristics for which relay to ask for a given event.

In the past, naive content replication has been used to solve the routing problem. Instead of developing methods for relay selection, all content was sent to every relay. One project in particular called Blastr encouraged people to publish their events to a Blastr relay, which would then re-publish it to hundreds of other relays.

This not only makes these "write proxies" a chokepoint for new content, but also is increasingly expensive as the amount of content being published to the network grows. With aggressive content replication, hundreds of duplicates of each event are foisted upon relays that may have no interest in storing them.

This is not horizontal scaling; it's redundant vertical scaling. If every relay has to hold every event, small relays become impossible, centralizing the network in a few mega-relays which can afford to store and serve everything. This isn't really economical at any scale, but is outright prohibitive when databases reach a billion plus events.

Aggressive replication is a brute force solution to the problem. In theory it would allow clients to ask any relay for any event, providing a 100% query hit rate. In reality though, this would actually destroy the network.

The alternative to brute forcing through content replication is intelligent relay selection. In order for decentralization to work, clients have to be responsible to "route" events and requests for events to the correct custodian in a way that is predictable. In this sense, redundancy is only relevant for degenerate cases, where the correct custodian fails to store the events it is responsible for. Routing heuristics are a form of interoperability that doesn't have to do with data modeling, but with network organization.

In order to solve this problem, we must have rules for:

- Where to send a given event
- Where to send a given filter

In the latter case there is less information available for solving the routing problem, which means multiple heuristics might be relevant for a given event, depending on how it might be queried.

# The Outbox Model And Friends

This is where the "Outbox Model" comes in. The Outbox model combines cryptographic identity with selective content replication, and was the first heuristic defined for solving the routing problem, but is certainly not the only one - other heuristics have emerged over time as the same problem cropped up in different contexts. At the end of this section, I'll enumerate several variations and their accompanying heuristics.

For now, I want to focus in some detail on the Outbox in particular, since understanding it is crucial for keeping decentralized, and the heuristics it defines are paradigmatic for the rest.

In the early days, nostr was used primarily for microblogging, and so NIP 65 was created in order to solve this problem _in that specific context_. NIP 65 therefore allows users to publish a `kind 10002` "relay selections" event, "to advertise relays where the user generally writes to".

By publishing their relay selections, users are declaring to the rest of the network that events they _create for public consumption_ can be found there. This covers things like blog posts, microblogging events, and user profiles.

So, in order to find a given user's blog posts (for example), I first have to look up their `10002` event (we'll cover how this happens in a bit), find the user's "write" relays in that list, then ask those relays for blog posts by the target user.

This is a very simple heuristic on its own, but it's important to be clear that it is not sufficient for every use case. The term "outbox model" is often used as a way to refer to the general idea of heuristics for relay selection, but in fact the outbox model is only one such heuristic, and is relevant only in the particular (though very common) context of author-based retrieval of public social media content.

The outbox heuristic is not sufficient to solve the routing problem in general for two reasons. First, there are many notes that should not be posted to user outboxes - for example, a 22242 auth response, or a chat message posted to a NIP 29 group. Second, any event may be retrieved based on some other criteria.

A second heuristic, also defined by NIP 65 is the "inbox model", which is intended to make social media posts discoverable based on users @-mentioned in the event. This heuristic is distinct from, but complementary to, the outbox heuristic.

For example, a note by Alice which mentions Bob should be posted both to Alice's outbox relays, as well as to Bob's inbox relays. To retrieve Alices's replies, we would use the outbox heuristic based on her `kind 10002` event - but if we want to retrieve Bob's mentions, we would use the inbox heuristic based on his `kind 10002` event.

Similarly, when posting to a NIP-72 community, you may or may not choose to also post an event to inbox or outbox relays, depending on how private you want the event to be. But in addition, it's important to post events to the locations defined by the group definition's `relays` tag. The reason for this is simple: when fetching a list of community posts, searching the outboxes of all the members of the community may not be feasible.

Posting to certain relays based on all applicable heuristics can be thought of as equivalent to creating multiple indexes on a database table, each to support a different query scenario. An index connects a query condition which supports a particular use case with where on disk matching records are stored. In the same way, a routing heuristic connects a filter that might be constructed to support a particular use case with the relay where matching events are stored.

Just like database indexes, relay selection heuristics are generally additive, and should all be applied when relevant so that the event in question can be found using the heuristic most appropriate to a given context. The exception to this is when some form of access control is desired - i.e., that the event _not_ be discoverable using a particular heuristic.

An example of this is content posted to NIP 29 groups. Because access control is part of the purpose of the NIP 29 spec, it would be a violation of the user's intentions to publish an event posted to a group according to the `outbox` heuristic - doing so would "leak" content which was intended to be protected.

This means, of course, that the usual `inbox` heuristic is not available for notifying users when they are mentioned in a group context. This might be considered a feature or a bug depending on your perspective; this is one of the tradeoffs involved in a system without a single arbiter governing access to content.

There are also situations where events might be available in locations not predicted by any standard heuristic, but instead as a result of a relay's content curation policy. You could make requests against (for example) an archival relay using any filter, and get whatever it returns. This is an ad-hoc heuristic, defined by the relay's policy and based on the relay's identity, not on any standard protocol feature. Relays have the right to override any heuristic, whether using negentropy to synchronize, attracting users to use their relay in a particular way, or by rejecting content that doesn't fit their policies.

Needless to say, this can get very complex. This is a natural result of the openness of the protocol and its permissionless extensibility. For publishers, the list of heuristics available to any given event should be well-defined, either by general-purpose heuristics like `inbox` and `outbox`, or by an additional or overriding heuristic defined for the event's `kind`. On the read side, however, no implementation will have a complete view of every heuristic that is applicable in a given situation, which means that there will inevitably be a certain amount of spontaneity to event discovery, particularly when the heuristic is user- or relay-defined. It's also important to note that applications only need to implement the heuristics relevant to use cases they support. An exhaustive routing policy is neither possible nor necessary.

Because the routing problem is both complex and important, let me give a few more example scenarios.

- NIP-17 direct messages should be sent to the recipient's `kind 10050` direct message inbox relay. Direct messages are encrypted to only one private key, which means each message gets sent multiple times - once to each user.
- The `outbox` relays NIP 47 zap receipts are sent to should be those of the zap _request_ author, not the zap _receipt_ author, since the wallet is only acting on behalf of the person sending the zap. In some cases though, it might be best to put the zap on an access controlled relay (for example, if you're zapping within a community group).
- Some events, such as NIP 72's `kind 34550` group metadata events, define which relays related events should be posted to using a `relays` tag.

Which relay an event is posted to depends primarily on how that event is to be read. Events need to be discoverable, which means readers need to be able to anticipate where the event is stored. However, there are some kinds which don't provide any of this information to someone wishing to request them - for example, `kind 37515` geocache listings, or any event with a `t` tag representing a social media topic.

In both cases, events belong somewhere that isn't currently well-defined by the protocol. The lack of a path from bootstrapping relays to content discovery is an flaw in the design of certain NIPs. Currently, this is solved by asking users to manually select the relays where they want to look for geocache listings or topics. This can be a perfectly valid heuristic on its own, but will necessarily result either in centralization (by clients who hard-code certain relays), or missed notes (since the ability to retrieve matching events depends on something between randomness and brute force). Additional signaling may be implemented to solve these problems, for example relays may advertise their support for certain `t` tags, or for geocache listings in a given region. In order for this to work though, the heuristics have to be defined and followed.

# Bootstrapping

For that you need another heuristic, but of a different kind. Currently the Outbox model is supported by known indexing relays that serve, that aggressively replicate and serve kind 1002 events. Once kind 1002 events are retrieved, any other event that abides by the outbox model, including 10,050 DM inboxes, can then be found on the author's outbox relays.

But this doesn't solve the geocaching index problem because geocaching indexes are not related to pubkeys but to relays, which means a separate type of indexing relay could be used to store the geocaches. The same indexers could store geocache index events or 10,002 could be overloaded to indicate support for geocaching relays.

But as I mentioned in the data modeling section of this book, overloading kinds is always a bad idea. Breaking things down into more event types means that things may not be as easy because you don't automatically get indexing for your geocaching index events. But it does mean that things are broken down more granularly, and relays and clients can choose what data they prefer to download. So when bootstrapping a new heuristic like geocaching, it's necessary to begin by selecting new indexer relays or expanding the policy of existing indexer relays to include the geocaching index events. This is an inherently political process that doesn't scale well in terms of censorship resistance out of the gate.

For someone who has created a geocaching client and they wish to bootstrap this heuristic, they're going to be the only one running a geocaching index relay. But that's OK. They're the only client interested in the use case. And so until that standard is adopted by other members in the network, it's effectively a walled garden. But the data format is open. So anyone else can create a client that uses geocaching events, or if they're an avid geocacher, another relay that indexes geocache index events.

And so the resilience of the index scales with the network effect built around the data type. This is in contrast to DHT-based solutions like IPCAR, which uses the mainline DHT. The mainline DHT is extremely censorship-resistant and huge.

But it makes no difference in how aggressively a given piece of content or a given index entry is replicated. Even if only one person cares about a given index entry, that entry will be replicated across the entire DHT as long as the user continues to refresh it.

This is not a terrible thing, in fact, it would probably be useful to add indexing on mainline or another DHT. Mainline uses a different cipher suite so secp256k1 keys can't be used as DHT addresses.

This would provide meta-redundancy in that it would allow bootstrapping to occur using any number of different technologies with different trade-offs, but the bootstrapping problem is always there. You're always going to have to start somewhere, whether it's a gateway or a simple relay.

Luckily the problem of indexing is orthogonal to Nostr. It may not fit tidily into mainline DHT, but there are plenty of other decentralized technologies that can be used to host indexes.









Something that frequently gets confused with heuristics for relay selection is relay hints. A relay hint is useful in certain places in the protocol, or is recommended in certain places of the protocol for short-circuiting the usual heuristic for discovering events, particularly in places where there's not sufficient information for fetching a given event. An example of this is kind 1111 comments. A comment is created.

A comment always exists in relation to another event. In general, it e-tags or a-tags that event and provides an event ID. Or in the most common case, it will e-tag that event and provide an event ID. An event ID tells you nothing about where to find an event, either the relay directly or the author who published the event, which would allow you to look up the author's outbox where the event ought to be stored.

For this reason, this NIP and several others defines relay hints on these e-tags. So after the event ID is included, a relay URL, which allows the client to attempt to fetch that event from that relay. Unfortunately, for the same reason that link rot happens across the internet, these relay URLs are not 100% reliable. And as a result, public key hints have been added as well. A public key is much more durable because as long as you can find the outbox relay selection for that public key, the user's relay selections can change, relays can go offline and come online, and there's still a well-defined path towards discovering the event in question.

In this way, relay hints are a complementary heuristic to the other heuristics mentioned above, useful in case those heuristics fail, which can happen due to buggy implementations or users changing relay selections without migrating their data, or any number of reasons.

Relay hints have another function though, which is to force relays to federate. If an event is published to a censorious relay and includes a relay hint that points to another relay, there's no way for the hosting relay to remove that reference without invalidating the signature of the event. And so that relay is forced to decide whether to reject the event entirely or to accept it and thereby advertise its competitor.

So therefore, even if a public key is banned from a given relay, their events can still be discovered either by relay hint or by public key hint. In fact, even if a public key is banned from all the main bootstrap indexers that hold kind 1002 relay selection events, the relay hint will often be, well, should usually be one of the user's outbox relays. And so hints can be aggregated and followed in case of a missing kind 1002 and reused in the case of looking up those public keys.

All this requires some fairly complex and sophisticated code to implement, and it could certainly be distilled into a more coherent framework. But solving this problem is essential to making Nostr censorship resistant. And because of the many different use cases that Nostr supports with its open data model, an unlimited number of heuristics may be appropriate. But it is possible to distill relay selection into a few given patterns. In a public broadcast context, relay selections created by the users and discovered on bootstrapping indexers are the most reliable way to go. These might be kind 1002 outboxes or they might be more use case specific. But if you know what user you want to fetch events from, you'll be able to find a cryptographically signed attestation from that user about where their events exist.

Another more difficult use case is when creating an event that defines where its children should live, like in the NIP-72 community definition. This event doesn't belong anywhere. And so finding the event is a matter of serendipity based on most likely who created the event. So this heuristic branches off of the outbox model, and these events then define the relays that ought to be used in the context that they create. Finally, you have scenarios like the geocaching scenario where you have third party indexer events not signed by event authors, but by some third party that's interested in those events being discoverable along a different axis than user or parent event.

There's an additional wrinkle to relay selections which needs to be addressed here and in implementations as well. Normally this problem is ignored because it's kind of complicated to think about and requires user action. But the problem is what happens if the relays selected by a given heuristic change over time? An example of this would be a user changing his outbox relays or his inbox relay selections or a NIP-72 community changing its suggested relays or a NIP-29 community being forked to another relay.

The answer to this problem is actually very simple. It just requires synchronization. If a relay hint changes, well, in any case, it's the responsibility of the person publishing an event to publish it where it needs to be, where other people expect to find it.

A corollary to this is that if anyone is changing the rules that determine where a given event should be found, they also are responsible for publishing events to that location. So in concrete terms, if I change my relay selections for my outbox relay from relay A to relay B, people are going to begin looking at Relay B to find my events. And they're gonna find nothing because I never published any events there. Meanwhile, Relay A is going to be wasting resources storing my events when no one is actually looking at relay A for my events any longer. In order to solve this I need to copy my events from relay A to relay B which is simple in principle, although Nostr probably needs better primitives for requesting synchronization from relays rather than downloading and re-uploading. But that works for now just fine. And then less importantly, but also worth doing, is requesting that Relay A delete my events. In practice, no one cares if someone is storing their events for free, so this likely won't ever be implemented, but Relay A should be then free to delete the user's events. And in fact, relays should actively be doing this. Unless they have a different heuristic or different policy for the content that they curate, relays should refuse to store user events if the user has not set that relay as their outbox or if the event does not tag someone who set the relay as their inbox. This has nothing to do with paying the relay or anything like that. If an event exists on a relay, and there is no heuristic for why that event might be there, it doesn't need to be there. Now the danger of this of course is that relays might not know every heuristic or might not care to implement every heuristic for finding a given event.

For example, they may not know the geocache index event that points people to their relay. But it still remains the relay's prerogative to delete whatever they want. And so people designing heuristics should be careful to choose relays that are incentivized to store the kind of content they want to store or who are aware of it. So geocaching specific relays are a good solution to this.

This change of heuristics over time or change of relay selections over time might be managed by a party who did not publish the notes as well. So if a NIP-72 community changes its relay selections then the community owner should be the one replicating the events from one place to another. It would also be possible in the event that clients don't implement this behavior, which is admittedly a pretty heavy lift. Watch towers could watch the network and based on known heuristics replicate content from one place to another.

Now let's talk about some different uses of relays and different kinds of relays that exist at the periphery of the network. One use of relays is as transport. A relay may not be the final destination of a given event, but only a broker for storing the event while it's in transit. A number of Nostr sub-protocols use this design in order to treat services running on a computer not exposed to the public internet as servers by piggybacking on relays. An example of this is NIP-46 Nostr Connect, which allows remote signers to monitor a relay for requests for signature or encryption or decryption requests. The signer holds the user's key, and the client asks the signer, via a relay and Nostr events, to do something with the key and return the result. The details of the flow are not important here, essentially because the relay is publicly addressable, both the client and the signer can use it to broker communication between the two.

And in this particular flow, a client would encrypt a message, send it to the relay, and the signer would listen to that relay for messages addressed to it, download them, decrypt them, process them, and publish a new event which would go backwards through the same process. Other examples are Nostr Wallet Connect, which allow for the connection of Bitcoin wallets, and any number of DVMs or data vending machines which do arbitrary calculations based on the spec associated with the kind of the event sent and received.

For many people less interested in the social media dimension of Nostr, this is Nostr's killer feature because it allows anyone to set up a service identified only by a public key and not by an IP address and for that service to be addressable and active on the network. This is useful for privacy purposes as well as for convenience and not having to deal with a lot of networking infrastructure. Recall that one of the big problems with P2P technology is the difficulty of NAT traversal. This completely bypasses that problem by piggybacking on a publicly addressable relay. And of course, because relays are interchangeable in terms of protocol, multiple relays can be used at the same time to broker communication.

So that's relays used as generic broker for transport for brokering communication.

Another way that relays provide utility is simply as a pattern for other protocols to use. In its simplest form, a relay independent of Nostr is a server that implements a protocol and which is advertised for selection by the end user on the Nostr network.

This allows for building lists of relays with metadata attached and providing tools to help users select which of these relays is appropriate for their trust model or use case. For example, you may not want to use a relay that's located in Russia, but you may be more comfortable with one run in the United States.

And this same selection process and the same kinds of heuristics can be applied to other things as well. Most notably Blossom servers, which are media storage servers that run on a protocol distinct from Nostr but tied in with it in certain ways. There is a kind event, for example, that allows Nostr users to advertise which Blossom servers they prefer to use so that other people can find their media even if the URL changes.

This allows users to select Blossom servers based on social signals and similarly media can be replicated across multiple Blossom servers or multiple Blossom servers may be used in parallel in order to find a given piece of content.

Blossom is basically applying the same pattern of interchangeable protocol servers that was pioneered by Nostr to media storage. Another example is Git repositories, which all speak the Git protocol. Or Cashu Mints, which speak the Cashu protocol.

All these things, whether Nostr aware or not, can be referenced by the Nostr protocol and used in parallel as redundant data stores.

This was a long chapter, the length is appropriate because relays are the most important part of Nostr, even more, I would argue, than signed data. Both are necessary conditions for Nostr to work, but the network architecture is what is really novel compared with digital signatures, which have been around for 50 years.

And I'm sure many parts of this chapter left you utterly confused as to what I am talking about. The complexity is a necessary result of the complexity of the many different use cases supported by Nostr. But included is a fair amount of incidental complexity, I'll be the first to admit.

It may be that a successor protocol comes along and borrows the good parts of Nostr without any of the bad parts. But for now, it's enough to understand that if you want to build on Nostr, you have to know what relays events belong on. And hopefully this helps make that somewhat clearer.
