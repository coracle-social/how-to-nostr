All protocols exist on a spectrom between open and closed.

Open protocols invite anyone to participate and build; closed protocols reserve participation to a select few. Closed protocols don't have a published specfication, don't have publicly available source code that can be used to reverse engineer the it, and can only be used by authorized developers. Access might be restricted by law, obscurity, complexity, or secrecy. Some closed protocols even lock things down with cryptography using techniques like DRM or VIN locking.

But no matter how much control its owners may try to exert, every protocol is at least somewhat open in the sense that it can be reverse engineered. This idea is proven repeatedly throughout the history of both analog and digital technology. Openness is part of an open system. Both physics and computing, (for example) are "radically" open.

However, just as it's true that no completely closed protocol exists, every "open" protocol is closed to some extent. The closing of open protocols may be intentional (as with the W3C's membership requirements) or it may be accidental due to poor communication - if salient protocol information isn't readily available, developers may have to resort to reverse engineering to make progress.

For this reason, openness is not equivalent to anarchism. The conflation of the two can actually cause a protocol to become more obscure through neglect. A similar fallacy is the equation of leadership with control. The job of a standards body is to document, not create, protocols.

As the IETF puts it in their mission statement:

> [our] mission is to produce high quality, relevant technical and engineering documents that influence the way people design, use, and manage the Internet in such a way as to make the Internet work better. These documents include protocol standards, best current practices, and informational documents of various kinds."

Designs might come from committee participants' research and opinions, or they might come from independent projects that independently gain adoption. In many cases this works well, particularly at a small scale. But when large commercial entities get involved, standards can end up benefiting the committee members rather than the beneficiaries of the technology. As Cory Doctorow puts it in his "The Internet Con":

> Patent ambushes are against the rules, but other forms of standards capture are fair game: for example, if the chair, co-chair and secretar all come from a single company (or a duopoly), that's fine, despite the fact that this means that the largest companies are literally setting the agenda.

An example of this is how browser development works. Frequently, Google designs some new API (for example, web components), builds it into Chrome, and because Google owns so much of the market, other implementations are forced to adopt. Unless of course you're Apple, which forces all apps on iOS to use their inferior browser engine, Webkit, in order to make native apps look better in comparison.

The exploitation of protocols is a well-known dynamic, a common pattern being to "Embrace, Extend, Extinguish". This is what Google did with XMPP and Google Talk. First, they found an open protocol that solved a problem and adopted it, immediately benefiting from the network effects that had been built up on that protocol. They then extended the protocol with incompatible alternatives to standard protocol features for chat archival, file transfers, and more. Initially, Google supported federation but didn't fully implement all standard security features, causing a number of servers to refuse connections to Google's servers. Eventually, Google dropped federation entirely.

Examples abound: Microsoft created incompatible versions of Java, HTML, Kerberos, CIFS, and LDAP; Apple added platform-specific APIs to Safari; Oracle created proprietary PL/SQL extensions; Google extended the web with their Accelerated Mobile Pages.

This approach is a threat to Nostr just like it's a threat to every other open protocol. But what's different about Nostr is that it is **radically** open. The Nostr Protocol is not something that is contained in a spec document that only certain people can write to, but is defined by the actual implementations.

This is arguably true of most open protocols, which are more often collections of patterns found in the wild than top-down specifications that dictate implementation. But Nostr explicitly embraces this paradigm. Nostr, like the internet, is not monolithic. There are some fundamental assumptions (like keys being secp256k1, or that events are serialized properly), but the vast majority of it is optional, and loosely coupled with the rest. As a result, any specification can only be partially comprehensive, and is necessarily relative to the perspective of its author (just like web of trust). In the same way that anyone can write an implementation, anyone can also write a specification describing their work, or even what they think should be the case.

There is an important qualification to this though. One application with no users can create a new event kind with a custom data format, but that doesn't mean anyone else will want to adopt it. On the other hand, a widely used application can create new data formats (or hijack existing ones) pretty much at will, and others will follow suit.

Every protocol feature exists on a spectrum between zero and universal adoption. Because the entire point of a protocol is to standardize something between implementations, this means that the extent to which a given standard is adopted determines how much a part of "the protocol" it is.

# Politics and Protocol

Efforts to standardize the Nostr Protocol are more akin to discovery than invention. There is a massive design space for the Nostr Protocol, and it's individual developers who explore that design space to find new solutions to problems. The people that document those solutions are only recording what has been built in the wild. This book is a good example; in it I offer a fair amount of prescriptive advice - but it's up to you to decide whether to follow it.

There's been some criticism of the various "centralized" actors in Nostr, most notably certain funding organizations and the maintainers of the specifications found on the NIPs repository. The idea is that a decentralized protocol should have decentralized funding, decentralized software, and a decentralized specification if it's going to live up to its permissionless ethos. And if a decentralized protocol is successful, then all these aspects of governance should be built on the protocol itself, right?

But technology does not solve problems, people do; protocol development is necessarily dependent on politics.

For some people, "politics" is a trigger word which evokes images of stale bureaucracies and misaligned elected representatives. But I mean it in the Aristotelian sense - a community of people working together to create an environment which they intend to inhabit. This is just another way of saying that a protocol, by definition, has to be developed by people working together in a structured way.

This is very difficult to get right, partly because politics is hard, but also because good protocol development is a result of successful resistance against monetary incentives. Incentives encourage capture, unless the different participants in the system rely on each other for success.

Right now, the Nostr community is far smaller and less consequential than, for example, the Bitcoin development community. Because fewer corporations are involved, we have fewer malincentives to deal with, which means we have a higher tolerance for political centralization. This has certain advantages with respect to communication efficiency. But the need for decentralization will increase as the monetary value associated with the ability to capture the protocol increases.

Because Nostr developers tend to be a pretty disagreeable bunch, fragmentation of the protocol is already happening. I personally worry that the centrifugal force of this disintegration might have the effect of actually making the protocol _more_ closed, not through permissioned politics, but as a result of the complexity inherent in making different parts of the protocol more obscure. In either case, politics is dysfunctional, and developers may have to resort to reverse-engineering the protocol in order to interoperate.

That said, protocol decentralization will need to happen sooner or later. The radically decentralized approach is one of Nostr's risky bets, and we may as well fail (or succeed) fast. And the sooner we start practicing decentralized protocol development, the sooner we learn how to do it well.

May people already self-host their own NIPs, or even create alternative curations of protocol features. See [Appendix B](./0b-resources.md) for a non-exhasutive list. The main problem with this is that it makes consensus more difficult and therefore weakens interoperability. If there are 50 different sources for protocol features, it becomes hard to discover them all. Right now, the NIPs repository is the place where the most visibility exists into new protocol proposals.

But the Nostr Protocol could eventually be moved to Nostr. There have been attempts at this, such as [NostrHub](https://nostrhub.io) and [Wikifreedia](https://wikifreedia.xyz/), though they haven't been fully developed or adopted, and have some outstanding problems. At a minimum, here's what would be necessary to make such a project viable:

- The ability to fork a spec and view the version history across all forks. Replaceable events don't work for this because they don't include old versions.
- The ability for implementations to signal spec and version support is required to help others decide which to implement in order to be interoperable. Ideally, the reputation of a given opinion would be based on ownership of relevant NIP 89 listings and their attendant user recommendations. This ensures inconsequential implementations don't derail interoperability, and could be set up to avoid over-weighting extremely popular implementations by capping reputation-based weighting.
- A forum for developers to propose new specs before they're implemented in order to get feedback on their design.
- A forum for tracking and resolving interoperability issues.

This kind of thing is hard to organize even in the best case, as the history and relative success of Stack Exchange makes clear. Decentralized consensus is a very high bar. The crypto graveyard is littered with decentralized autonomous organizations (DAOs).

Luckily, incentives work in our favor because interoperability is the key value proposition of Nostr. This is why the NIPs repo specifies that any NIP should have at least two client implementations and a relay implementation if relevant. This ensures that nothing makes it into the NIP repo that isn't already an interoperable part of the protocol or a part of the protocol that supports interoperability.

This criteria also helps reduce scope, since a lot of things don't need to be interoperable. For example, mobile push notifications are cryptographically tied to a particular app, which means there's no real point in including them - systems can't talk to each other anyway.

# Thinking in Public

One thing that has obscured the actual dynamics of Nostr's protocol development is the use of the NIPs repo for speculative proposals as well as for documentation of existing work.

In contrast with the actual contents of the repository, the issues and PRs that are hosted on GitHub frequently are requests for comment rather than established protocol features. This goes back to the necessity for political involvement around protocol development. There's a trade-off between implementing the first idea that pops into your head, and enduring a long period of review before calling the idea "official". No review results in garbage specifications getting adopted. Too much review enervates would be contributors, who lose interest and go elsewhere.

Some protocols, like MLS, have been in development for years without practical application. This is probably a good idea because the entire idea is to have a watertight security and privacy model. But this isn't really how Nostr works. I think of Nostr as the Javascript of the web protocol world. Javascript, born at Netscape in 1995, was designed and implemented in just ten days by Brendan Eich. Eich had to reconcile his ideas about programming language design, which were borrowed from Scheme, with an appeal to the current popularity of Java for marketing reasons.

The result was Javascript, a language with multiple null values, quirky type coercion, and several arcane features like [labels](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) that ultimately fell by the wayside, but which remain in the protocol document. In addition, in the early days, JavaScript implementations were notoriously fragile and incompatible between browsers (partially due to lack of standardization, partly due to browser vendors trying to capture the market).

Much better languages could have been designed for the purpose of scripting in web browsers. But JavaScript hit the ground running, and now it is the single most used programming language in the world.

Nostr is full of half-baked ideas written by application developers (as opposed to protocol developers) who are learning the discipline of protocol development on the fly. Nostr is a mess. Incompatibilities between implementations abound. Data types that are prone to race conditions are a core part of the protocol. Kinds get overloaded. Services go offline.

But this is all by design. And I won't say that there aren't large existential risks associated with this development approach. But given Javascript's success, it's hard to say that it's a much worse model for protocol development than anything else.

In fact, most successful protocols are more or less like this. Protocols (and software) designed in a top-down manner frequently end up failing to live up to their design goals. It's only through implementation that what is actually needed can be understood, and it's only through implementation that multiple implementations can exist to interoperate in the first place. Nostr takes the implementation-first approach to an extreme.

# Backwards Compatiblity

Prioritizing implementations doesn't mean that the process of design, review, and feedback is not necessary though. In Nostr's openness and "shoot first ask questions later" environment, a lot of discussion and review still happens, just well after protocol features become "official." Just because something is in the NIPs repo doesn't make it sacred.

Migrating away from existing standards has been one of the most divisive issues in the Nostr developer community to date. Maintaining backwards compatibility is a massively important principle in software development, whether you're creating a system that's proprietary or an open protocol.

When deploying an update to a proprietary system, it's important that the old version of the application continue to be able to talk to the database, that the old version of the client continue to be able to talk to the backend, etc. But this requirement is ephemeral because the organization running the infrastructure has the ability to eventually upgrade the entire stack and throw away the old code.

In protocol development, backwards compatibility is a much harder problem. In order to fully implement backwards compatibility, you can never really remove a feature. We see this with HTML, where blink and marquee tags created in the 1990s still exist. Programming languages commonly maintain backwards compatibility to make migrations easier - when Python 3 broke compatibility with Python 2, it took almost ten years for users to migrate.

But there is a cost to compatibility: the monotonic increase in implementation complexity. Complexity makes implementation more expensive. This in turn makes the protocol vulnerable to capture by entities with the resources to deal with this complexity.

In a descriptive, lean protocol like Nostr, backwards compatibility remains important (particularly due to the importance of avoiding disruption of network effects), but in a much more practical sense. Backwards compatibility has a purpose, and that purpose is to maintain a good user experience. We don't need to be dogmatic about backwards compatibility. As Ralph Waldo Emerson said, "a foolish consistency is the hobgoblin of little minds."

Backwards incompatible protocol changes aren't as destructive as people frequently make them out to be. This is particularly true because the universal desire for interoperability necessarily encourages conservatism in breaking compatibility.

First of all, the breadth of the nostr protocol makes it possible to change on part of the protocol without affecting the rest. Only the clients which actually implement the feature affected by a change have to care about it. This can be a relatively large number if the feature affected involves follow lists, or microblogging content. But it might be much smaller if it involves some more obscure part of the protocol with only two or three implementations. In contrast, HTML has to be compatible across _billions_ of websites.

In addition, there can really be no changes by fiat (even if, as sometimes happens, backwards-incompatible changes make it into a specification document without community buy-in). Nostr is an adversarial environment, and relies on developers to actually implement changes they want to see. To the extent that an implementation has active users, it can choose to go along with the fork, or hold back.

In this way, implementations that want to sponsor either a new protocol feature or an incompatible change can exert pressure on the rest of the network by threatening more or less incompatibility. Likewise, implementations that wish to keep the protocol as is, or not implement a new feature can do the same. This can be done by shaming competitors in public while maintaining interoperability, or by actually breaking compatibility. Forks always come with the risk of alienating users or being on the losing end of network effects, which is a natural restraint to reckless behavior.

This dynamic is currently playing out with Nostr direct messages. Nostr's original direct messaging implementation, NIP-04, leaks a lot of metadata, undermining user privacy to the point that bots were created that monitor and publish information about who is conversing with whom.


--------------






This problem was severe enough that a new DM standard was created which leaks less metadata. As of the time of this writing, this new version is adopted in the majority of the most popular Nostr clients with two important exceptions.

These clients have lagged behind in adoption because, partly because of a commitment to backwards compatibility, and partly because of a different set of priorities. Both of these clients are focused on high quality UX, and yet ironically, their users are being left behind on an outdated standard that is losing support across the rest of the network. Right now, Nostr DMs are useless because of these holdouts, or depending on your perspective, because of the people who chose the fork. But to the extent that the lack of support for old style DMs makes user experience poor, one faction or other of these will lose users to the other faction. Or potentially the protocol will lose its users, which is why backwards incompatibility should be used with care.

This means that there is always a certain amount of chaos involved in Nostr Protocol interoperability. But as Pablo F7Z says, embrace the chaos.

The chaos is a necessary consequence of a radically open protocol.

---

I've been talking a lot about what interoperability is and how to support it, but I haven't mentioned what interoperability is for. What good is it for multiple implementations to talk to each other?

This goes back to the problem that Nostr is trying to solve, which is Big Tech's capture of social media platforms and by proxy, their users. In legacy social media, users don't have what's called a credible exit, which is to say that they can't leave a platform and retain their identity or their data.

In order for this to work, not only does data have to be open and unconstrained by custodian, which is what relays and signatures give us, there also have to be multiple implementations. A user has to be able to have a choice. If there's only one implementation, because of protocol complexity or because the protocol is proprietary, then users don't have the ability to exit because they can't enter something else. In order for users to move, there need to be off-ramps and on-ramps.

Openness makes it possible for multiple implementations to interoperate. But we've already said that and that's a fairly low bar. This is true of ZeroMQ, which is a messaging protocol, or JSON, which is a data format. Two computers can talk to each other if they both understand JSON and send it over ZeroMQ.

This means that those project users have credible exit in the sense that they can choose different libraries to handle their JSON parsing and message brokering needs.

But those users are at a very low level and they're building products that don't have the same sort of openness in most cases. In fact, open source funding is a big problem because proprietary software is built on top of it and the proprietary software companies, which make all the money off of the open source developers' hard work, don't tend to contribute back to the developers making the open source software and giving them credible exit and open protocols.

This is akin to building a closed source Nostr client on the open protocol.

Open source software is less fundamental than an open protocol, but it's still extremely important.

Because the protocol is descriptive, implementations that are widely adopted might create ad hoc undocumented protocol features. If the software isn't open, it becomes much harder to reverse engineer these protocol features in order to allow others to adopt them. I've personally looked at dozens of different code bases, source code, in order to understand how something works.

My go-to is Nostrudel because Hazard and Amethyst because their developers try to implement as much of the protocol as they can, and their code is very readable and clean.

Because Amethyst is open source, I was able to understand how private zaps worked.

Open implementations support an open protocol by making the actual working of the protocol accessible to developers, but it also benefits users directly.

AI-assisted coding is good for certain things and bad at other things. But one thing it is very good for is allowing non-technical users to take off-the-shelf software and adapt it to their needs without having to understand what's going on under the hood.

With AI assistance, it's easy to take a piece of open source software, run it, and change it as desired to have some feature that you've always wanted or to fix a bug that bothers you, or change the layout and color.

These are all well within the ability of normal users.

Even if something goes wrong, the AI hallucinates and creates a fork in the protocol. These one-off implementations, because they're built by an end user, rarely see much adoption. The user is just trying to scratch their own itch. If they create malformed events or use some data format in an incorrect way, the damage that they cause is limited only to their malformed content or user experience. And because they have taken responsibility for their user experience by creating their own solution, it's up to them to fix this if they're motivated.

This dynamic is maybe more important than it sounds at first. I think this is one of the most important things about open protocols and one of the most exciting things about AI-assisted coding.

Used properly, AI-assisted coding has the ability to tear down walled gardens at a scale that we can't even imagine.

If we can encourage users, if AI has the effect of amplifying user agency in the digital world, users become more capable of shaping the digital world based on their values and goals, which are invariably at odds with the software platforms that we're trapped inside in the current iteration of the internet.

Like I said earlier, it's not technology that fixes things. It's people who fix things. Technology is an extension of human will into the world. And yes, there can be unintended consequences. But when individuals use what Ivan Illich calls convivial tools, their agency is multiplied and the negative externalities are limited to the scale at which that individual operates.

This creates a diverse ecosystem of self-interested actors who can not only do what they want in the digital world, but protect themselves from other people who would want to take advantage of them, either through massive structures of control or through exploitation of centralized systems through hacking or phishing.

It could very well be that AI assistance, both in coding and in research and many other ways, is far more important than the existence of an open protocol. It may even obviate the need for an open protocol because the LLM can reverse engineer whatever software the users are already using.

A latent possibility for this that has existed for decades is that most centralized platforms run in the browser and therefore have to present HTML and JavaScript, which even if obfuscated can still be understood with enough study. Users can today already make browser extensions that remove ads, hide content, add buttons, but very few people actually do, even among developers.

It could be that this is just a result of human nature and inertia, but I'm hopeful that the ease with which AI agents can be used to take advantage of these injection points will lead to increased prevalence of the hacker mentality among regular people.

However, an open protocol can't hurt. An open protocol makes the entire database and identity layer hackable as well as the presentation layer.

Instead of simply being able to add a button, users can add much deeper integrations into the mechanisms behind the data flow through open source applications running on an open protocol modified through LLMs.

With the increasing saturation of human life with digital means, this hacker mentality is more important than ever to safeguard human freedom and maintain human agency.

It's tempting to want to opt out of the internet entirely when we look at its effects. But the only way forward is through. And I strongly believe that cultivating the hacker mentality is the way forward.

---

Given the radical openness of the Nostr protocol, some additional mechanisms are necessary in order to cope with the certainty of running into event kinds that implementations don't recognize.

It's categorically impossible for clients to implement support for every Nostr data format because new data formats are created constantly.

So what do you do when you run into an unknown event kind?

Suppose a user embeds an event to a kind 30023 long form article in a kind one microblogging post and your client doesn't want to add render support for long form articles. How can you handle that event without knowing what it is?

A few mechanisms have been proposed for dealing with this. I think they're not completely there yet. We could have more robust systems, but the beginnings are there. First of all is NIP-31, which proposes the inclusion of an alt tag on events, which describes, in human readable language, what the event is. And so, your client could look at the long form article, see an alt tag with the title of the article and an explanation of what that event actually is and display that to the user. This is something, but it's not very compelling. This is a dead end and all the user knows is that they aren't seeing content that they would like to see. There's no call to action for how to actually view the content unless a link is included in the alt tag.

But that likewise would be centralizing because it would likely rely on a particular implementation.

An additional problem with this is that it in practice conflates data with content. This alt tag, if it replaces the actual content of the article, might confuse users who might interpret it as being the actual content of the thing. It's important when designing UX to have visual signals that this isn't actually the content of the article.

I think alt tags were a good attempt, but ultimately a bad idea.

More sophisticated means are required for giving users a path forward when presented with unrecognized data.

A simple error message would probably be an improvement over alt messages because it would demonstrate to the user that something is indeed missing or broken.

Luckily we have an alternative in NIP-89 application handlers.

NIP-89 builds affordances into the protocol that users can use as a path forward when presented with unknown data, and NIP-89 combines that solution with social graph traversal.

NIP-89 combines this affordance with cryptographic identity by providing a kind 31989 recommendation event for kind 31990 application handlers.

An application handler is a kind 31990 event which includes tags that include information that describe the application and its purpose as well as affordances for opening a given event or profile in that application.

Application handlers also include a k-tag, which can be used to filter out handler events when looking for application handlers on the network.

So in our scenario above, the microblogging client, when presented with a long form article, could ask the network for kind 31990s with a k tag matching 30023.

This would return a bunch of application handlers with web, Android, iOS, or other handler tags. And the client can then present that to the user in order to give the user options for how they want to view the content.

This allows implementations to reduce their scope to not implement features that they don't care about supporting, while at the same time improving the state of the network by advertising alternatives or complementary applications to their users. This is not something that a walled garden would ever want to do. Their impulse is always to verticalize or to vertically integrate their stack and eat every adjacent industry. On Nostr, because implementations can enjoy the network effect of the entire protocol without implementing the whole protocol, they can afford to recommend alternatives. And in fact, doing so makes their value proposition stronger, because users now have a myriad of alternatives to pick from. This is good user experience. If users are served, they will stay.

NIP-89 enhances this ability to search for handlers even further by recognizing that anyone can publish a handler event and these handlers might not necessarily be trusted. Maybe they're trying to phish your users or advertise to them or maybe the application provides a poor UX even if it's well-intentioned.

Kind 31989 recommendation events allow anyone to publish a signal about which clients they use to handle a particular kind. And so when prompting a user with an application handler list, clients are able to include social web of trust data that validates a given application handler. Maybe only one person that the user follows uses an application handler, or maybe a hundred people do.

Clearly, the more popular app is more likely to provide the user with a good experience. However, the one recommendation might provide an interesting alternative to the popular app, thus eroding the hold that popular applications have on the network.

This can help mitigate the concentration of power in a few popular implementations.

Application handlers are not the only kind of recommendation event on Nostr by any stretch. Follows can be seen as recommendations loosely of other accounts. Recommendation events exist for relays in the form of reviews and Cashu mints in the form of various kinds.

Unfortunately, data vending machines, which are essentially service providers that use relays as transport brokers, overloaded kind 31990 application handler events.

Because DVMs have their own kinds that they handle, this works okay in practice, but would have been much better as an alternative listing event.

This migration could be a worthwhile backwards incompatible change to campaign for on the protocol, because there's confusion about what handling actually means as long as both applications and service providers are using the same listing types.

For example, if a user wants an application that can handle kind 5300 content recommendations, does that mean they want to send those kind of events from a given client or do they want to send those events to a particular service provider? This is a good illustration of why it's bad to overload kinds and why creating new kinds for new use cases is almost always the right choice.

Even if DVMs and application handlers were separated out, there could still be some ambiguity. For example, between publishing and rendering certain kinds.

These could be subdivided further, but the cost of backwards incompatibility in this case may not be worth starting from scratch. These kinds of decisions are things that individual developers and individual users can decide for themselves and campaign for through their use of their preferred patterns in the adversarial environment that is Nostr.

The important thing to recognize about recommendation and handler events is that they make possible a social media ecosystem in a way incomparable to what has gone before.

In a forest, trees trade sugars to fungi in exchange for minerals extracted from the soil. These wildly different life forms have a mutually beneficial relationship that results from the exchange of these resources.

Likewise, Nostr clients and users can benefit from the structured exchange of signed events and functionality.

An ecosystem is an environment in which life forms inhabit. The media ecosystem is a complex digital environment that humans inhabit.

More complexity does not necessarily mean more alienation. If the correct affordances are provided to users, they can become able to intuitively navigate the complexity of the system to be meaningfully agential in a digital space.

This vision represents a huge improvement over the status quo. Implementation is another story.

But viewing implementations as an ecosystem surrounding and serving end users is an important and helpful frame for guiding their development.

