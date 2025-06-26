# Nostr Improvement Possibilities

Throughout this chapter I'm going to make mention of "NIPs", so I'd better begin by defining the term. "NIP" stands for "Nostr Improvement Possibility" - i.e., a specification related to nostr. These specs might define new content types, or new behaviors for relays, clients, or other related services.

Because nostr is open, anyone can write a spec and publish it anywhere they want. Unfortunately, this also means that there's no comprehensive list of specs anywhere (although undocumented.nostrkinds.info is a useful tool for avoiding re-use of event kinds).

While Nostr is about as anarchic a protocol as you can get, there remains an irreducible political component to protocol design. Software cannot be interoperable if communication doesn't exist. Now, this communication might simply take the form of reverse-engineering other people's events and code, but communication is (obviously) improved through the use of language.

Right now, the best place to collaborate is at https://github.com/nostr-protocol/nips. This is a carefully curated collection of Nostr specs, and the place the most Nostr developers participate. There has been some talk about creating a solution that exists purely on Nostr where we can get permissionless participation, a comprehensive list of specs, and a system for consensus, but such a solution has not yet been built.

With that in mind, let's get into events - the "what" of Nostr.

# A Single Data Type

All data on Nostr, with very few exceptions, is contained in "events". Here's an example of an event:

```jsonc
{
  "id": "b13ef435ad614ee37b74f6d6e8055c303a79b95354dcb65b075fb3964a6731e0",
  "pubkey": "3bf0c63fcb93463407af97a5e5ee64fa883d107ef9e558472c4eb9aaaefa459d",
  "created_at": 1682377261,
  "kind": 1,
  "tags": [
    ["p", "73c7f6d5bb599bb7d7cee84c72e89dbd549df53da522ed6c7611055cc0db64bc"],
    ["a", "31337:73c7f6d5bb599bb7d7cee84c72e89dbd549df53da522ed6c7611055cc0db64bc:5jqxarp0z1kr7yem"]
  ],
  "content": "is this Lana Del Rey?",
  "sig": "91d7ae3d5a7ef72e917b52829f0dd76538be2b1720f3c09d0bf71131cffd81f18b89956ef2bab9ea44e656edd96529d0d3fc71c29e305a5378fb4087bfb08f7a"
}
```

Here's what those fields mean:

- `id` is a hash of the event (serialization is defined in NIP 01)
- `pubkey` is the public key of the event author
- `created_at` is the second-granularity unix timestamp the event was created
- `kind` is the content type of the event, which determines how it should be handled
- `tags` is a list of lists of strings, which provide metadata for the event
- `content` is a (usually) human-readable representation of the event for display
- `sig` is a `secp256k1` cryptographic signature of the event `id`

The core of the event is the cryptographic properties: `id`, `pubkey`, and `sig`. These three properties make it possible to 1. verify the event author, and 2. refer to the event by content hash rather than location. We'll talk more about this later, but it's hard to understate just how important these properties are. For now though, I want to get into a different topic: data modeling.

# Numbers, not Names

Every event has a "kind," which is a 16-bit integer. A kind is Nostr's equivalent of a "content type". In other words, an event's `kind` determines how that event should be interpreted. Using numbers instead of names is an unconventional choice, but it has certain benefits.

In a distributed system built on signed data, names can't change. Once you choose a particular term, you're stuck with it forever. The nice thing about integers is that they're meaningless, which allows for a diversity of interpretations while still retaining a single standard.

Names have the weakness that they import meaning with them into their new context. This meaning might vary from person to person, or the person who chose the name might have made a poor choice. This results in confusion over the purpose and semantics of a given data type.

Numbers carry no such meaning (except in a memetic sense, like how Nostr uses `kind 1984` for content reporting). This frees up every implementer to assign their own term to an event based on their understanding of it. If their understanding of the content type changes, they can change the term they're using for it without affecting anyone else. This allows language conventions to develop independently of the technical characteristics of a thing.

Another possible approach to this problem is that of "reverse domain notation." This is a great way to create an identifier that does not collide with anyone else's, but (apart from having the same semantic difficulties as unqualified names) it also implies some level of ownership of a.

Nostr is a permissionless protocol. Any event that is signed and sent is valid simply by virtue of existing, at least to the extent that it is accepted as valid by the network. Because there is such a diversity of content types and the protocol is open for extension, it's impossible to validate every event kind based on data structure, which naturally limits validation to hash and signature validation, and a very few other things.

This is very different from how we usually think about protocols. Normally, protocols use natural language to describe data structures or processes that must be followed. On Nostr, kinds are their own vocabulary. Because they are numeric, they have no metaphorical referent, which means that usage determines meaning.

This is the same way that natural language works. Usage evolves over time, resulting in a mess of neologisms, malapropisms, idioms, and ambiguities. Dictionaries were invented only as a way of understanding language as it already exists. The Oxford English Dictionary includes not only definitions, but also the history and etymology of words, defined by actual use.

The same word might vary from place to place. You might have the same word with different meanings in different places. Language is organic and very difficult to systematize. Nostr embraces this ambiguity, which is admittedly a risky choice, since we don't know if software-mediated language can evolve in the same way as human-to-human language.

But because of this design choice, Nostr is essentially a humble protocol - no more than an empty shell which users can then fill. This isn't to say that there aren't conventions that should be followed when designing new content types.

They most important design principle is to avoid using a single kind for multiple purposes. If there are two content types that are very similar but differ in minor ways, it's almost always a better choice to split it into multiple kinds. For example, NIP 52 uses separate kinds for time-based and date-based events. This not only reduces ambiguity, but also allows clients to work more easily with one or the other or both content types.

Likewise, some data makes sense to group together in a single event, for example kind `0` profile metadata. But the more data is attached to a single event, the more contention there will be over writing to that event, and the more conflicts become possible. If I had to redesign profile metadata today, I would create separate events for user name, profile picture, bio, lightning address, nostr address, and every other field on the event. This would be marginally more data for clients to download, but it would prevent data loss in the event of incomplete synchronization. This is even more true in the case of follow lists.

There is a guideline listed in the nips repository, that "there should be no more than one way of doing the same thing." Because nostr is a social protocol, it depends on network effects, not just of users, but of standards. The more implementations that use a single kind, the more users are in turn able to interact. So when creating a new standard, check to see if there is an existing spec and follow it if at all possible. This might seem to contradict my advice to error on the side of proliferating data types, but it's important to understand that the "one way" rule is only an _ideal_, and can still be violated if design goals vary, or an existing spec is broken in some cricial way. Just be prepared to defend your divergence from convention if you want other people to migrate to the new way of doing things.

# Immutability and Replaceable Events

# Timestamps are liars

There are an incredible number of [falsehoods programmers believe about time](https://infiniteundo.com/post/25326999628/falsehoods-programmers-believe-about-time). Dealing with time is inherently difficult, especially in a distributed system which has no single timestamping authority.

For this reason, Nostr's core protocol entirely punts on the problem - the `created_at` timestamp on events is supplied by the user, who can falsify the timestamp with no real constraints. There are certain mitigations of this, for example NIP 03 allows for the use of Open Timestamp attestations to prove an event was published after a certain point in time, but Nostr chooses to solve this problem by moving it from the technical to the social layer. In other words, if you don't trust someone to be honest about their timestamps, why are you reading their content anyway? Reputation is key in social media, and provides a natural solution to many technical problems.

Furthermore, Nostr leans into this by only supporting second-granularity timestamps. This is consistent with the very simple, human-oriented approach to social media that Nostr aims for. On a human time scale, sub-second granularity rarely matters. The temptation with millisecond granularity is that you might expect to be able to reliably sort events by when they occurred in a reliable way.

But in a distributed system, that's not actually true. Clock skew across different computers is commonly more than one second, so messages may show up out of order even if you're relying on millisecond-granularity timestamps for sorting.

A possible solution to this is to use something like vector clocks where every piece of data increments a counter, or to build linked-list style data structures where every event refers to a previous piece of data in the chain. Not specifying a mechanism for ordering keeps the protocol flexible, and allows for natural solutions to emerge for each individual use case. Some content types form a natural tree structure, where ordering can be inferred by client implementations. Others explicitly provide affordances for enforcing order.

This is a good place to introduce a key part of the nostr design ethic: trust users, trust developers, and keep things simple. Protocol documents are often bloated with clarifications for every edge case, resulting in standards no one actually reads. Nostr specifications should be brief and to the point so that the most people possible can understand them and hack on the protocol.

# Content and Tags

Finally, we have `content`, and `tags`. An event's content is generally a human-readable payload, while tags are structured data.

In reality, content isn't always human-readable. There are several event kinds that encode JSON or encrypted data into the content field. That pattern should be seen as an exception - this precedent was set early in the protocol when conventions for designing events weren't well established. Data should generally go in the tags array, and human-readable information should go in the content field.

You might be wondering why tags is a list of lists, rather than an associative data structure. The advantage of list lists of lists structure is 1. you can include the same key twice, and 2. tags preserve order. You see similar data types with ordered dictionaries in Python, and URL query parameter. This allows for more flexible data modeling than simple dictionaries would provide.

Tags are always an array of strings, not numbers or composite data structures. This keeps parsers simple (at the cost of sometimes doing dumb things like encoding numbers as strings or nesting JSON-encoded strings in JSON data structures). Usually there are at least two entries, conventionally (though not necessarily) being treated as key/value pairs. Some specifications  include four or more positional items in a tag, while other include only one.

For example, the NIP-70 protected tag, `['-']`, has no values. The presence of the tag merely indicates that the event that the protected tag is on should only be published to relays by its author.

Another example is the NIP 18 q-tag, which is used to reference a quoted event. This tag contains an event ID, a relay URL where the event might be found, and the pubkey of the event's author, for example: `["q", "29916f5671eb3f93ee1d3f655ef14109591f6905ff1328a76fccc27bf6b449a6", "wss://relay.example.com/", "12fec3c26b3efdaa521db0bd02056cca90d401aafff0233635f78da2f4cb8d44"]`.

In general, tags should be as short as is reasonable. Two to three entries is all you really need; if you have more than that, you're probably trying to pack more data into a single tag than really belongs. A better approach is to create other tags that form an index that can be used to look up additional metadata. This makes it easier for consumers to parse the tags array instead of having brittle positional arguments.

For example, the above `q` tag could be split into `q`, `relay_hint`, and `pubkey_hint` tags:

```jsonc
[
  ["q", "29916f5671eb3f93ee1d3f655ef14109591f6905ff1328a76fccc27bf6b449a6"],
  ["relay_hint", "29916f5671eb3f93ee1d3f655ef14109591f6905ff1328a76fccc27bf6b449a6", "wss://relay.example.com/"],
  ["pubkey_hint", "29916f5671eb3f93ee1d3f655ef14109591f6905ff1328a76fccc27bf6b449a6", "12fec3c26b3efdaa521db0bd02056cca90d401aafff0233635f78da2f4cb8d44"]
]
```

The benefit here is that new information about the event ID can be added associatively. It also allows for adding multiple values for a single key (like if you wanted to include multiple relay hints). Of course, the cost is that this pattern makes events more verbose.

This is the same trade-off as exists in programming languages when choosing named vs positional arguments (for example python's `*` construct). Named arguments make it a lot easier to maintain backwards compatibility as a function's signature evolves, and the same is true of nostr events.

# Filtering Events

# Modifiers and Data

# A Light Touch

Dealing with other people's signed events is always going to require some adversarial thinking. Events can be malformed, either from a buggy implementation or from an attacker trying to crash implementations. A `p` tag might have an invalid or missing value, or a relay hint that is trying to spy on users. Event `content` might include HTML injection attacks, or illegal content.

Distinguishing between when to discard an event and when to try to handle it anyway is difficult. The most important thing when handling events is to protect the user from attacks. Everything else should be handled in a fault-tolerant way, assuming incompetence rather than hostility.

It's important to note though that Postel's "be liberal in what you accept" has two different possible interpretations here. Fault tolerance does NOT mean repairing data that contradicts established conventions. A common example of this is when clients publish events with bech32-encoded data in tags instead of hex-encoded data.

This is of course a difficult judgment call, since as mentioned above the vocabulary of nostr is idiomatic and evolving. The important thing is not to allow a minority, non-standard data format to hijack a well-established content type. This can go some way toward taming the chaos of a decentralized system, as well as protect against organized attacks that would attempt to "embrace, extend, extinguish" the protocol.

Here are a few examples or malformed data and how it should be handled:

- If an event's signature is invalid, discard it - there's no way to prove it isn't forged. There are of course exceptions to this, like with NIP 59 wrapped events, which have no signature, but are still authenticated cryptographically.
- If an event contains code intended to crash, denial-of-service, or hijack the client, the client should protect itself using conventional defensive programming techniques - by sanitizing HTML before displaying it, not using regular expressions with user provided data, and by handling errors using null checks and fallback values.
- If an event contains an adversarial relay hint or suspicious media URL, clients should have a policy policy in place, informed by user preferences, which blocks connections to unknown or untrustworthy hosts. This can be accomplished through domain white/black listing, or through trust assessments based on event proof of work or the reputation of the author.
- If an event contains data that doesn't adhere to the relevant specification, for example missing `start` or `end` times on a calendar event, clients might choose to show a fallback value, e.g. "not specified", or an error indicator.

One reason to prefer fault-tolerant handling over aggressive validation is that strict validation reduces interoperability unnecessarily by converting minor, recoverable errors into catastrophic exceptions that ultimately result in a poor UX. Care has to be taken to balance user protection, user experience, and long-term stewardship of the protocol when making these decisions.

An additional wrinkle to this problem involves writing rather than reading events. A number of bugs have emerged where data published by one client will be unwittingly deleted by another client. Here are a few examples:

- Some clients at one point started adding JSON-encoded relay selections to the `content` field of kind `3` follower list events. Other clients would drop these selections when updating user follows.
- Some clients started adding muted words to kind `10000` mute lists, in addition to muted pubkeys. Clients that weren't expecting this ended up dropping muted words when updating muted pubkeys.
- Similarly, some clients began adding private mutes to kind `100000` mute lists by JSON-encoding the tags, encrypting the result, and placing it in the event's `content` field. This resulted in mutes being ignored, overwritten on update, or even being permanent for clients that only read from, but didn't write to the encrypted mutes field.

In every case, these bugs are a result of poor design - overloading a single kind for multiple purposes is always a recipe for disaster. But in cases where poor designs become conventional, it can be helpful to handle events in such a way that unanticipated data doesn't get dropped.

One way I've found to do this is to write parsers for an event in order to turn it into a standard data structure that can be used elsewhere in my application with the original event attached. Then, when saving a new version of the event, I update the event directly, keeping tags and content intact as much as possible before re-publishing.

This adds a certain amount of additional effort to implementations, but is very important for avoiding disruption of user experience.

# Backwards Compatibility

Backwards incompatibility is one of the big problems of spec design. When breaking backwards compatibility, not only do you break other existing implementations, but in a system where events can't be migrated to the new format you also break all historical data, even if it was published by your own app.

At the same time, breaking backwards compatibility can free you up to improve the protocol in important ways. In many cases, it also won't have much of an impact. Supporting historical data is important for some applications, like archival services, but many applications have a stron recency bias such that they don't necessarily mind throwing away old data.

I think there's a balance to this. I don't think we can be backwards compatibility maximalists, but we also shouldn't be careless about throwing away old formats for no reason. There is a perverse impulse among software developers to refactor for dumb reasons which should absolutely avoided.

When introducing new backwards-compatible functionality to Nostr, it's usually best to enhance existing data formats as long as it doesn't result in overloading a single kind with multiple uses. When breaking backwards compatiblity, however, it's best to create an entirely new kind and evangelize for migrating to it. This is much harder than modifying the behavior of existing event kinds, but it's far more polite. The downside is it breaks network effects - and can still result in a poor UX for clients that don't adopt the new format if it results in missing content.

Over time, Nostr protocol development has gotten increasingly conservative. As use cases proliferate, it becomes more difficult to review new data formats. As implementations proliferate, it becomes more difficult to advocate for breaking changes. Nostr specifications are not sacred, but their effectiveness relies almost entirely on interoperability. Maintaining compatibility requires conscientousness, communication, and contributions to other projects - there's no better way to get people to listen to you than writing code to improve their implementation.
