# Chapter 4: Relays are Repositories

Thus far we've focused mostly on "Nostr as data." But data modeling, signatures, and identity are really only half of the story. Nostr is much more than a data format — what is much more interesting is its network architecture.

## Why WebSockets

Many cutting-edge decentralized protocols are "peer-to-peer," which means they attempt to repurpose the architecture of the internet to facilitate direct communication between peers. Peer-to-peer technology is really neat, but it's also hard to get right because it works against the grain of the internet as it has been used for the last 30 years.

That's not to say P2P technologies are of no use. Mesh network systems and P2P communication techniques can be great when used as fallbacks from more traditional infrastructure and networking technologies. But just like it would be very hard or impossible to completely replace the hub-and-spoke architecture of the internet with a mesh network, P2P systems are not a complete replacement for the client-server model.

Nostr attempts to get many of the benefits of P2P-style architectures without a lot of the hassle by using a pretty boring piece of web technology: WebSocket servers. WebSocket servers have all the same problems that regular servers have in terms of being gate-kept by internet service providers, since normally they rely on TLS root certificates, ISPs, and DNS registrars. Domain name resolution can be bypassed, but then users have to deal with IP addresses. TLS can be bypassed, but then implementations have to run things through Tor, which has its own trade-offs.

Most nostr relays use TLS with conventional domain names. And in true Nostr fashion, this is good enough™. Because anyone can buy a domain name and spin up a server, there are hundreds of relays out there that can be used for storing signed data. If relay operators or users want to up the ante (for example if the country they live in [man-in-the-middle attacks TLS](https://en.wikipedia.org/wiki/Kazakhstan_man-in-the-middle_attack)), they can always resort to more advanced techniques. And if a particular relay goes offline, it's only one of many redundant nodes.

In "Simple Made Easy," Rich Hickey defines the distinction between easy and simple. "Easy" means something is "close at hand". Something that's easy may not be the best solution, but it's accessible. "Simple" means that something does one thing well without being complicated by different concerns. In technical terms, relays are not really simple. Relays are easy. Relays use WebSockets which are a layer on top of HTTP which is a layer on top of TCP/IP, which is itself a fairly complicated protocol.

The trade-off here is that the technology, again, is not ideal, but good enough. WebSocket servers also allow for duplex communication rather than request-response, which allows servers to push new information to the client as soon as they receive it.

But using WebSockets doesn't preclude the use of other transport protocols to send events between peers.

As an aside, I'm not talking about Nostr over HTTP. HTTP, while simple and more familiar for developers who are used to working with web technologies, is strictly worse than using WebSockets because HTTP doesn't allow duplex communication, increases latency through polling (or requiring support for [server-sent-events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)), and makes clients and relays less efficient. If you're going to rely on the web stack, just use WebSockets.

What I mean rather is alternative transport protocols that have a different simplicity/ease trade-off balance from WebSockets. In theory you could come up with a binary encoding of Nostr events and send them over QUIC, which would eliminate a lot of the overhead associated with WebSockets. This might be useful for high performance applications and servers.

Alternatively, you might put a bunch of Nostr events in a JSONL file and torrent it. These events would then be replicated on a different decentralized network and could be downloaded by a client supporting that transport, improving censorship resistance (assuming the dataset is valuable enough for people to seed it).

Another example would be to use P2P technologies as progressive enhancement. In other words, you could [enhance the connectivity of Nostr applications](https://github.com/nostr-protocol/nips/pull/1979) in certain scenarios without breaking the base protocol. This might be a useful when designing a mobile application for people in rural areas with little network coverage. If the network isn't available, devices would fall back to direct connection over Bluetooth or WiFi Direct.

This technique was pioneered by Secure Scuttlebutt (SSB), which started with P2P technologies and then added pubs as a way of bridging devices that weren't directly connected. Nostr simply reverses this model and makes pubs the primary means of communication and optionally adds P2P when required. Of course, these alternative transport protocols have by and large not been specified or implemented, but there's nothing to keep us from creating them.

In terms of transport protocol, Nostr opted for "easy" by default. But this dimension of the relay network is secondary to the network architecture itself, which adheres much more closely to Hickey's idea of "simplicity". So, setting aside the transport questions for now, let's get into what relays actually do.

## Multi-Master

A key aspect of Nostr's architecture is its reliance on more than one relay for storing data. As we mentioned in the previous chapter, relays can't falsify anything because your data is signed. They don't have the ability to lock users in or create a data moat. What they do have, however, is the ability to censor or delete user data.

If you use only a single relay, that relay has complete control over which of your signed events get rebroadcast to other people. It may even selectively censor data depending on who's asking for it or what you're publishing. Adding an additional relay decreases your vulnerability to censorship in a straight-forward way. If, say, you have a 10% chance, all things being equal, of being de-platformed by a single relay, publishing to two relays gives you a 1% chance; three relays gives you a 0.1% chance. Beyond that, if you're particularly sensitive to the risk of de-platforming, your best option is probably to self-host or select relays you can explicitly trust to host your content.

The fallacy that "more is better" is evident with relay operators — many people run a relay just so they can "run a node". But (to borrow a term from Bitcoin), you have to have "an economical node". In other words, people have to use it — and you have to keep it running.

For the average social media user, three to five popular relays is generally enough. As long as the relays provide a good mix of different admins, jurisdictions, and policies, you're very unlikely to lose all your hosts at once. Even if you do, you still have your key! Just keep a periodic backup of your content and re-broadcast it when you find more trustworthy hosts.

This ignores the problem of which relays should be used to store what content. Solving this problem is the key to making Nostr's multi-master architecture work; naïve replicas result in either excessive duplication of content across all relays, or persistent failure to locate content. We'll get to that soon, but first I want to define what a relay actually is.

## Functional Relays

Relays are simple repositories of events. They hold a bunch of events in some database or other and grant access to those events using the Nostr WebSocket protocol. This protocol involves sending JSON-encoded messages over WebSockets using just a few core commands:

- Clients can send an `EVENT` message in order to publish an event to a relay
- Relays respond to client `EVENT` messages with an `OK` message, which includes whether the event was accepted or rejected and an human-readable message with details
- On the read side, clients can send a `REQ` with a subscription ID and a filter
- Relays can respond by sending one or more `EVENT` messages, each of which contains an event

There are a few other control messages, including `CLOSE`, which allows a client to close a `REQ`; `CLOSED`, which allows a relay to close a `REQ`, and `EOSE`, which allows relays to let clients know when they've sent all events initially matched by a `REQ` (the relay might continue to stream matching events as it receives them).

There are some other details which we'll get to below, but this is pretty much it! A relay is just a bucket that you put events into. Later, you or someone else might take them out again.

Some additional commands have been proposed, and in some cases added to the protocol, but to the extent that they stray outside of this basic repository paradigm they only complicate things for little or no benefit. One example is `COUNT`, which might seem useful at first until you consider that in order to count events in a decentralized network you need a way to reconcile those events between multiple servers. COUNT doesn't do that, making it useful only when working with a single relay.

For the sake of decentralization, it's my opinion that the relay interfaces should be minimal in order to reduce implementation burden and maximize interoperability.

That said, there is one additional responsibility that relays can't really delegate: access control. Access control on Nostr is implemented by the `AUTH` verb. When a relay wants to know who opened a connection, it issues an `AUTH` message with a challenge string. The client then incorporates this challenge string into a `kind 22242` event, signs it, and sends it back to the relay.

From this point on, the relay can implement any policy it wants on the basis of the user's cryptographic identity by rejecting published events, refusing to serve requests, or selectively filtering data before returning it to the client.

This is useful for two distinct things: content curation and access control. Many relays have policies about what kind of content is allowed on their relay, whether based on content analysis, social graph analysis, proof of work, or when an event was published. Much of this data is already available on any event that gets published to a relay, but the identity of the person publishing an event can also be an important way to vet content cross-posted from elsewhere on the network, or if the user is paying to store content on the relay.

Access control is similar to, but distinct from, content curation. Relays may or may not care what events in particular they store, but they may want to allow access only to particular users. This can be useful for community relays, relays that handle direct messages, or relays that proxy content on behalf of paid subscribers. Likewise, relays may allow anyone to request events, but be very selective of what content is actually stored.

These policies together make relays less fungible — which is, counter-intuitively, a good thing. Some large hubs accept everything except for obvious spam, and are therefore mostly interchangeable — there's no reason to establish a relationship with one rather than the other. Other relays implement custom policies for protecting community content or direct messages, which make them more appropriate for certain use cases. Another example would be relays which return an algorithmic selection of notes from across the network, making social media "algorithms" possible.

This is an important point — to the extent that relays are treated as commodities they also have to be either subsidized by businesses operating on nostr, or run *pro bono*. Relays that don't have a distinctive value proposition don't have a business model. This presents the danger of leading us back into the surveillance capitalism of the existing internet. Presenting relays to the end user as distinct services providers forces users to consider who they do business with and why, creating affordances for direct monetization and alignment of incentives that wouldn't exist if relays were abstracted away.

One final thing to note in this context is [Negentropy](https://github.com/nostr-protocol/nips/blob/master/77.md), a set-based reconciliation protocol used for efficiently syncing events between two relays (or between a client and a relay). This allows a client to request only events it doesn't yet have, significantly reducing bandwidth requirements.

This does a lot to facilitate content replication across relays without burning through resources, which in turn makes it possible for the network to re-organize itself to align with expectations about where a given event "should" be stored.

## Replication and Routing

The Nostr network is highly partition tolerant, unlike (for example) Secure Scuttlebutt, which links all events from a single key together, making it impossible to download a single event without downloading all events that came before it. On Nostr, you can download any dataset you want, because events aren't tied together. The cost of this is that you never know if you have all the events; the benefit is that content can be replicated more selectively across the network.

This is actually how Twitter's architecture works too — in order to scale, they maintain a network of interrelated caching nodes. When the average user posts content it normally gets sent immediately to read caches for all of their followers. But when a very popular account posts content, it's replicated to special "famous person" caches, distributing load without excessive duplication. Their system is also overprovisioned and able to respond to dynamic load, since news events may happen without warning.

This is of course an over-simplified view of Twitter's [architecture](https://blog.x.com/engineering/en_us/topics/infrastructure/2017/the-infrastructure-behind-twitter-scale), but you can see how nostr relays might correspond to cache nodes. If Nostr is to scale, it will naturally adopt a similar architecture. This requires not only the availability of enough nodes to support the network, but (arguably more importantly) heuristics for which relay to ask for a given event.

In the past, naïve content replication has been used to solve the routing problem. Instead of developing methods for relay selection, all content was sent to every relay. One project in particular called Blastr encouraged people to publish their events to special write-proxy relays, which would then re-publish it to hundreds of other relays.

This not only makes these relays a chokepoint for new content, but is also increasingly expensive as the amount of content being published to the network grows. With aggressive content replication, hundreds of duplicates of each event are foisted upon relays that may have no interest in storing them.

This is not horizontal scaling; it's redundant vertical scaling. If every relay has to hold every event, small relays become impossible, centralizing the network in a few mega-relays which can afford to store and serve everything. This isn't really economical at any scale, but is outright prohibitive when databases reach a billion plus events.

Aggressive replication is a brute force solution to the problem. In theory it would allow clients to ask any relay for any event, providing a 100% query hit rate. In reality though, this would actually destroy the network.

The alternative to brute forcing through content replication is intelligent relay selection. In order for decentralization to work, clients have to be responsible to "route" events and requests for events to the correct custodian in a way that is predictable. In this sense, redundancy is only relevant for degenerate cases, where the correct custodian fails to store the events it is responsible for. Routing heuristics are a form of interoperability that doesn't have to do with data modeling, but with network organization.

In order to solve this problem, we must have rules for:

- Where to send a given event
- Where to send a given filter

In the latter case there is less information available for solving the routing problem, which means multiple heuristics might be relevant for a given event, depending on how it might be queried.

## The Outbox Model And Friends

This is where the "Outbox Model" comes in. The Outbox model combines cryptographic identity with selective content replication, and was the first heuristic defined for solving the routing problem, but is certainly not the only one - other heuristics have emerged over time as the same problem cropped up in different contexts. At the end of this section, I'll enumerate several variations and their accompanying heuristics.

For now, I want to focus in some detail on the Outbox in particular, since understanding it is crucial for keeping decentralized, and the heuristics it defines are paradigmatic for the rest.

In the early days, nostr was used primarily for microblogging, and so NIP 65 was created in order to solve this problem *in that specific context*. NIP 65 therefore allows users to publish a `kind 10002` "relay selections" event, "to advertise relays where the user generally writes to".

By publishing their relay selections, users are declaring to the rest of the network that events they *create for public consumption* can be found there. This covers things like blog posts, microblogging events, and user profiles.

So, in order to find a given user's blog posts (for example), I first have to look up their `10002` event (we'll cover how this happens in a bit), find the user's "write" relays in that list, then ask those relays for blog posts by the target user.

This is a very simple heuristic on its own, but it's important to be clear that it is not sufficient for every use case. The term "outbox model" is often used as a way to refer to the general idea of heuristics for relay selection, but in fact the outbox model is only one such heuristic, and is relevant only in the particular (though very common) context of author-based retrieval of public social media content.

The outbox heuristic is not sufficient to solve the routing problem in general for two reasons. First, there are many notes that should not be posted to user outboxes - for example, a 22242 auth response, or a chat message posted to a NIP 29 group. Second, any event may be retrieved based on some other criteria.

A second heuristic, also defined by NIP 65 is the "inbox model", which is intended to make social media posts discoverable based on users @-mentioned in the event. This heuristic is distinct from, but complementary to, the outbox heuristic.

For example, a note by Alice which mentions Bob should be posted both to Alice's outbox relays, as well as to Bob's inbox relays. To retrieve Alices's replies, we would use the outbox heuristic based on her `kind 10002` event - but if we want to retrieve Bob's mentions, we would use the inbox heuristic based on his `kind 10002` event.

Similarly, when posting to a NIP-72 community, you may or may not choose to also post an event to inbox or outbox relays, depending on how private you want the event to be. But in addition, it's important to post events to the locations defined by the group definition's `relays` tag. The reason for this is simple: when fetching a list of community posts, searching the outboxes of all the members of the community may not be feasible.

Posting to certain relays based on all applicable heuristics can be thought of as equivalent to creating multiple indexes on a database table, each to support a different query scenario. An index connects a query condition which supports a particular use case with where on disk matching records are stored. In the same way, a routing heuristic connects a filter that might be constructed to support a particular use case with the relay where matching events are stored.

Just like database indexes, relay selection heuristics are generally additive, and should all be applied when relevant so that the event in question can be found using the heuristic most appropriate to a given context. The exception to this is when some form of access control is desired - i.e., that the event *not* be discoverable using a particular heuristic.

An example of this is content posted to NIP 29 groups. Because access control is part of the purpose of the NIP 29 spec, it would be a violation of the user's intentions to publish an event posted to a group according to the `outbox` heuristic - doing so would "leak" content which was intended to be protected.

This means, of course, that the usual `inbox` heuristic is not available for notifying users when they are mentioned in a group context. This might be considered a feature or a bug depending on your perspective; this is one of the tradeoffs involved in a system without a single arbiter governing access to content.

There are also situations where events might be available in locations not predicted by any standard heuristic, but instead as a result of a relay's content curation policy. You could make requests against (for example) an archival relay using any filter, and get whatever it returns. This is an ad-hoc heuristic, defined by the relay's policy and based on the relay's identity, not on any standard protocol feature. Relays have the right to override any heuristic, whether using negentropy to synchronize, attracting users to use their relay in a particular way, or by rejecting content that doesn't fit their policies.

Needless to say, this can get very complex. This is a natural result of the openness of the protocol and its permissionless extensibility. For publishers, the list of heuristics available to any given event should be well-defined, either by general-purpose heuristics like `inbox` and `outbox`, or by an additional or overriding heuristic defined for the event's `kind`. On the read side, however, no implementation will have a complete view of every heuristic that is applicable in a given situation, which means that there will inevitably be a certain amount of spontaneity to event discovery, particularly when the heuristic is user- or relay-defined. It's also important to note that applications only need to implement the heuristics relevant to use cases they support. An exhaustive routing policy is neither possible nor necessary.

Because the routing problem is both complex and important, let me give a few more example scenarios.

- NIP-17 direct messages should be sent to the recipient's `kind 10050` direct message inbox relay. Direct messages are encrypted to only one private key, which means each message gets sent multiple times - once to each user.
- The `outbox` relays NIP 47 zap receipts are sent to should be those of the zap *request* author, not the zap *receipt* author, since the wallet is only acting on behalf of the person sending the zap. In some cases though, it might be best to put the zap on an access controlled relay (for example, if you're zapping within a community group).
- Some events, such as NIP 72's `kind 34550` group metadata events, define which relays related events should be posted to using a `relays` tag.

Which relay an event is posted to depends primarily on how that event is to be read. Events need to be discoverable, which means readers need to be able to anticipate where the event is stored. However, there are some kinds which don't provide any of this information to someone wishing to request them - for example, `kind 37515` geocache listings, or any event with a `t` tag representing a social media topic.

In both cases, events belong somewhere that isn't currently well-defined by the protocol. The lack of a path from bootstrapping relays to content discovery is an flaw in the design of certain NIPs. Currently, this is solved by asking users to manually select the relays where they want to look for geocache listings or topics. This can be a perfectly valid heuristic on its own, but will necessarily result either in centralization (by clients who hard-code certain relays), or missed notes (since the ability to retrieve matching events depends on something between randomness and brute force). Additional signaling may be implemented to solve these problems, for example relays may advertise their support for certain `t` tags, or for geocache listings in a given region. In order for this to work though, the heuristics have to be defined and followed.

## Bootstrapping

One event kind that I've thus far avoided introducing a heuristic for is `kind 10002` relay selections. If these determine where the rest of a user's public notes live, what determines where they belong? This is the classic bootstrapping problem of networks, for which you need a heuristic of a different kind.

In other words, you have to start somewhere. It's impossible to access a "network" without accessing particular nodes. When not yet connected, nodes have to be selected by some heuristic external to the network itself.

The most common way to solve this problem is to hard-code "indexer" or "default" relays in implementations, from which point other relays can be discovered using NIP 65, NIP 66, or relay hints. Alternatively, a distributed hash table (DHT) might be used to store events related to relay selection, improving censorship- and sybil-resistance.

In either case, events need to be stored in one of these few starting points in order to be discoverable. If they can't be found, none of the events they help locate can be found either (except accidentally).

In practice, hard-coded lists of bootstrapping relays work pretty well for the same reason that a small amount of redundancy in user relay selections can dramatically reduce the risk of censorship. Because hard-coded indexer relays are selected by implementation authors (or by users themselves), they're easy to swap out if any of them become censorious or go offline. This is strictly worse than using a DHT, but the strategies are not mutually exclusive. As time goes on, I expect a DHT-based solution to the bootstrap problem to be introduced as a progressive enhancement.

One difficulty with the bootstrap relay model, however, is that different types of bootstrapping events are needed to support different relay selection heuristics. The outbox/inbox heuristics are defined by `kind 10002`, but topic-, location-, community-, or language-based heuristics aren't, and any relay discovery events that support them will certainly be replicated less aggressively.

The solution to this is to take a step backward, and instead of focusing on `kind 10002` as the entry point to the network, switch to `kind 30166` relay discovery events for bootstrapping. Of course, since relay discovery events can be published by anyone, and aren't necessarily related to the user's web of trust, another heuristic has to be used to bootstrap trust - both indexer relays and indexer pubkeys might be hardcoded by implementation developers in order to avoid sybil attacks by untrusted relay monitors, or this trust might be delegated to the indexer relay operators. In either case, the user is delegating bootstrap relay selection to their client's developer.

Let me give an example to make this more concrete. Suppose you want to find relays that store `kind 21` video events about cats. Beginning with 2-5 semi-trusted relays which the client developer has chosen to curate relay discovery events, the client can first send a request for relay discovery events tagged with the desired topics, and which support the desired event kinds:

```json
["REQ", "subid", {kinds: [30166], "#t": ["cats", "cat", "catstr"], "#k": ["21"]}]
["EVENT", "subid", {
  "kind": 30166,
  "created_at": 1722173222,
  "content": "{}",
  "tags": [
    ["d", "wss://somerelay.abc/"],
    ["t", "cats"],
    ["k", "21"],
  ],
  "pubkey": "<pubkey>",
  "sig": "<signature>",
  "id": "<eventid>"
}]
```

The client can then apply additional heuristics (like relay reviews for example) to these results, then send a request for the desired content to each relay url advertised.

The same heuristic can be used for any event kind, provided at least one of your bootstrap relays is reliable. Hard-coding relays isn't ideal, certainly, but with these limitations in mind, it can be "good enough", consistent with the nostr ethos.

The downfall of all of this is to what extent developers are interested in supporting the decentralization of the nostr network. Hard coding a relay to read from and publish to is easy. Hard coding 2-5 bootstrap relays from which relay discovery events can be fetched for the purpose of finding relays hosting use-case-specific index events in order to find the desired content... is hard.

But that's why I'm writing this book. Decentralization is not easy - but it has massive payoffs if developers go to the trouble of building robust, principled implementations of the protocol.

## Relay Hints

Something that frequently gets confused with heuristics for relay selection is relay hints. Relay hints are baked into certain events, particularly where there isn't sufficient information otherwise available for fetching a related event.

An example of this is `kind 1111` comments, which always exist in relation to another event. In general, it e-tags or a-tags the parent event and provides an event ID or address. An address contains the author's pubkey, which allows for looking up the author's outbox, then asking for the event in question. But an event ID tells you nothing about where to find it.

Relay hints were designed to solve this problem. By adding a relay URL to the tag containing the event ID, the user now has at least some idea of where to look for it. Unfortunately, for the same reason that link rot happens across the internet, these relay URLs are not 100% reliable.

As a result, pubkey hints have been added as well. A public key is much more durable because as long as you can find the outbox relay selection for that public key, the user's relay selections can change, relays can go offline and come online, and there's still a well-defined path towards discovering the event in question.

Together, relay and pubkey hints comprise an additional heuristic which can be used as a fallback in case more reliable heuristics (like outbox) fail due to buggy implementations or users changing relay selections without migrating their data.

Relay hints have another function though, which is to force relays to federate. If an event including a relay hint is published to a censorious relay, the hint cannot be removed without invalidating the event's signature. As a result, relays are forced to decide either to reject these events entirely, or accept them and thereby advertise someone they would otherwise choose to censor.

This make is possible for a user's events to still be discoverable across the network, even their public key is banned from a significant portion of popular relays. Clients can take advantage of this dynamic in order to heal the network, prompting users to update their relay selections to route around censorship.

If this all seems very abstract, take a look at https://how-nostr-works.pages.dev/#/pathological - this page includes several animations that illustrate how relay hints help keep the network healthy.

Properly implementing robust relay selections across the many heuristics, bootstrap mechanisms, and relay hints is obviously complex, and could be made simpler if re-designed from scratch. But solving this problem is essential to making Nostr censorship resistant, and because of the many different use cases that Nostr supports with its open data model an unlimited number of heuristics may be appropriate.

## Content Migration

There's one more wrinkle to relay selections which needs to be addressed before we're done here. What happens if the relays selected by a given heuristic change over time? This most commonly happens when a user changes his outbox relays, but it can occur for any other relay selection heuristic. Normally this problem is ignored or overlooked in implementations, but because nostr relays are not intended to be trusted either now or perpetually, having a story for how to manage this problem is an essential part of any complete implementation.

Luckily, the solution is actually very simple in principle. Because events are signed, they can simply be replicated to the relays that are expected to be storing them withouth having to do anything complex, like establish a chain of custody from one relay to another.

In an open system like Nostr, no one can force anyone else to do the right thing, which means that the smooth functioning of the system depends on incentive structures. In order for an event to be discoverable, heuristics for locating it need to be anticipated by someone. But who exactly is responsible for sending events to the right place? The obvious answer would be the event author, but that's not actually correct. The person responsible for putting events in the correct place is the person *who wants the event to be discoverable in that place*.

This means that the onus is on users (and by extension their clients) to choose good outbox relays and publish their events to them. Group admins are responsible for properly configuring infrastructure to accept the correct relays and make them available. And people that curate topical data are responsible either to scrape the network or incentivize publishing to their relays.

Similarly, it is the responsibility of anyone that changes the result of relay selection heuristics to synchronize events to the new relay. If a relay changes his inbox relay, he should copy all events that mention him to the new location. If a group switches relays, group messages should be copied by the admin. If a new indexer relay gets stood up, the admin should copy relevant events from the network.

Here's a simple example of what happens if data isn't properly synchronized when relay selections change:

- Alice publishes a `kind 10002` with relay A as her `write` relay
- Alice publishes a `kind 1` to relay A
- Alice updates her `kind 10002` with relay B as her `write` relay
- Bob fetches her `kind 10002`, requests Alice's `kind 1`s from relay B, and finds nothing

Bob correctly followed the outbox heuristic, but failed to find content that does actuall exist on the network. In essence, Alice lied to Bob - she published a claim that her notes were available on relay B, when in fact they weren't. If she had copied her `kind 1` event from relay A to relay B, however, Bob's query would have been successful.

Less important but also worthwhile, is event deletion. This part of content migration is the responsibility of the relay operator, since they are the only person who has any incentive to free up their resources, although users could request deletion as a courtesy. This could get complex, since a relay won't necessarily have a complete view of every heuristic others are using to locate events on their relay. In any case, relays have the prerogative to delete whatever they want, so people storing data should be careful to choose relays that are properly aligned.

As of this writing, synchronization is absent from most or all implementations. In order for it to become possible, both protocol and implementations will have to be developed.

In terms of implementations, convenient tools will have to exist to do this on behalf of those with incentives to migrate events. Clients might do this in the background on behalf of their users when relay selections change, and community admin tools might include synchronization affordances for community relays. Alternatively, watchtowers could be used to actively synchrnonize data according to certain heuristics. Users might even be able to pay these services to ensure that their content is properly available.

In terms of the protocol, currently the only way to synchronize events to a new relay is to download all involved events and re-publish them manually, which can be fairly expensive in terms of bandwidth. A new primitive for asking a relay to synchronize certain relays from a peer would be a useful optimization. Similarly, there aren't currently any protocol affordances for requesting deletion of events - neither NIP 62 nor NIP 09 quite fit the bill, since they're more permanent.

## Relays as Transport

Earlier I defined relays as "a repository of events." This definition can be exploited to do some interesting things not originally intended though. Specifically, relays can be used as a form of transport broker.

A relay per se is rarely the final destination of a given event, but is rather an intermediary between producers and consumers. Communication via relays may be between humans (as with social media), or it may be used to allow different software applications to communicate. Both use cases are defined by the event `kind` that is used for payloads, and both are equally valid. This is the basis of some of Nostr's most interesting "other stuff".

An example of this is NIP-46 Nostr Connect, which allows remote signers to monitor a relay for signature (or encryption/decryption) requests. The signer application holds the user's key, and the client asks the signer, via a relay and Nostr events, to do something with the key and return the result. The details of the flow are not important here, but because the relay is publicly addressable, the client and the signer are able to communicate.

Other examples are Nostr Wallet Connect, which allow for applications to communicate with the user's bitcoin wallet, and any number of DVMs (or Data Vending Machines) which do arbitrary computations based on the event kind being used. In many cases, encryption is also employed to create a secure communication channel between parties.

For people less interested in the social media dimension of Nostr, this is Nostr's killer feature. Communication via relay allows anyone to set up a service identified only by a public key rather than an IP address. This is useful for protecting service providers' privacy, and makes running small services extremely convenient. Using this model, service providers can be run in any internet-connected software, without dealing with the complexity involved with NAT traversal. And of course, because relays are interchangeable in terms of protocol, multiple relays can be used at the same time to broker communication.

## The Relays Pattern

Zooming out even further, relays are useful as a conceptual pattern that can be applied in the context of another protocol. In its simplest form, a relay independent of Nostr is just a server that implements a protocol, and which is advertised for selection by the end user on the Nostr network.

For example, Blossom servers are media storage servers that run on a protocol distinct from Nostr, but are referred to using Nostr events. Defined in [BUD 03](https://github.com/hzrd149/blossom/blob/master/buds/03.md), `kind 10063` events allow Nostr users to advertise which Blossom servers they prefer to use so that other people can find their media even if the URL embedded in a social media post changes.

This allows for the same kind of heuristic used for relay selection to be applied to other media servers, piggybacking on Nostr for the indexing and trust layers. And just like events, media can be replicated across multiple Blossom servers, introducing redundancy to media hosting.

Blossom applies the same pattern pioneered by Nostr of interchangeable protocol servers to media storage. Another example is Cashu Mints, which speak the Cashu protocol. This pattern is not unique to the Nostr protocol ecosystem either - Git, ActivityPub, FTP, XMPP, and many other internet protocols also follow this pattern. But Nostr is an exceptionally clear example of how useful this pattern is when used in conjunction with signed data.

## Wrapping Up

This was a long chapter, for which I apologize. But its length is appropriate because relays are the most important part of Nostr. Even more important, I would argue, than signed data. Both are necessary conditions for Nostr to work, but the network architecture is what is really novel compared with digital signatures, which have been around for 50 years and yet haven't gained widespread end-user adoption.

I'm also sure many parts of this chapter left you utterly confused as to what I was talking about. The complexity involved in dealing with relays is in part a natural result of the many different use cases supported by Nostr. But I'll be the first to admit that a fair amount of incidental complexity has also snuck in as the protocol has developed.

It may be that a successor protocol comes along and borrows the good parts of Nostr without any of the bad parts. But for now, it's enough to understand what relays are, and how to use them.