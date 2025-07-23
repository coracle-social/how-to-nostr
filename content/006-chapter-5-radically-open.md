# Chapter 5: Radically Open

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

## Politics and Protocol

Efforts to standardize the Nostr Protocol are more akin to discovery than invention. There is a massive design space for the Nostr Protocol, and it's individual developers who explore that design space to find new solutions to problems. The people that document those solutions are only recording what has been built in the wild. This book is a good example; in it I offer a fair amount of prescriptive advice - but it's up to you to decide whether to follow it.

There's been some criticism of the various "centralized" actors in Nostr, most notably certain funding organizations and the maintainers of the specifications found on the NIPs repository. The idea is that a decentralized protocol should have decentralized funding, decentralized software, and a decentralized specification if it's going to live up to its permissionless ethos. And if a decentralized protocol is successful, then all these aspects of governance should be built on the protocol itself, right?

But technology does not solve problems, people do; protocol development is necessarily dependent on politics.

For some people, "politics" is a trigger word which evokes images of stale bureaucracies and misaligned elected representatives. But I mean it in the Aristotelian sense - a community of people working together to create an environment which they intend to inhabit. This is just another way of saying that a protocol, by definition, has to be developed by people working together in a structured way.

This is very difficult to get right, partly because politics is hard, but also because good protocol development is a result of successful resistance against monetary incentives. Incentives encourage capture, unless the different participants in the system rely on each other for success.

Right now, the Nostr community is far smaller and less consequential than, for example, the Bitcoin development community. Because fewer corporations are involved, we have fewer malincentives to deal with, which means we have a higher tolerance for political centralization. This has certain advantages with respect to communication efficiency. But the need for decentralization will increase as the monetary value associated with the ability to capture the protocol increases.

Because Nostr developers tend to be a pretty disagreeable bunch, fragmentation of the protocol is already happening. I personally worry that the centrifugal force of this disintegration might have the effect of actually making the protocol *more* closed, not through permissioned politics, but as a result of the complexity inherent in making different parts of the protocol more obscure. In either case, politics is dysfunctional, and developers may have to resort to reverse-engineering the protocol in order to interoperate.

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

## Thinking in Public

One thing that has obscured the actual dynamics of Nostr's protocol development is the use of the NIPs repo for speculative proposals as well as for documentation of existing work.

In contrast with the actual contents of the repository, the issues and PRs that are hosted on GitHub frequently are requests for comment rather than established protocol features. This goes back to the necessity for political involvement around protocol development. There's a trade-off between implementing the first idea that pops into your head, and enduring a long period of review before calling the idea "official". No review results in garbage specifications getting adopted. Too much review enervates would be contributors, who lose interest and go elsewhere.

Some protocols, like MLS, have been in development for years without practical application. This is probably a good idea because the entire idea is to have a watertight security and privacy model. But this isn't really how Nostr works. I think of Nostr as the Javascript of the web protocol world. Javascript, born at Netscape in 1995, was designed and implemented in just ten days by Brendan Eich. Eich had to reconcile his ideas about programming language design, which were borrowed from Scheme, with an appeal to the current popularity of Java for marketing reasons.

The result was Javascript, a language with multiple null values, quirky type coercion, and several arcane features like [labels](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) that ultimately fell by the wayside, but which remain in the protocol document. In addition, in the early days, JavaScript implementations were notoriously fragile and incompatible between browsers (partially due to lack of standardization, partly due to browser vendors trying to capture the market).

Much better languages could have been designed for the purpose of scripting in web browsers. But JavaScript hit the ground running, and now it is the single most used programming language in the world.

Nostr is full of half-baked ideas written by application developers (as opposed to protocol developers) who are learning the discipline of protocol development on the fly. Nostr is a mess. Incompatibilities between implementations abound. Data types that are prone to race conditions are a core part of the protocol. Kinds get overloaded. Services go offline.

But this is all by design. And I won't say that there aren't large existential risks associated with this development approach. But given Javascript's success, it's hard to say that it's a much worse model for protocol development than anything else.

In fact, most successful protocols are more or less like this. Protocols (and software) designed in a top-down manner frequently end up failing to live up to their design goals. It's only through implementation that what is actually needed can be understood, and it's only through implementation that multiple implementations can exist to interoperate in the first place. Nostr takes the implementation-first approach to an extreme.

## Backwards Compatiblity

Prioritizing implementations doesn't mean that the process of design, review, and feedback is not necessary though. In Nostr's openness and "shoot first ask questions later" environment, a lot of discussion and review still happens, just well after protocol features become "official." Just because something is in the NIPs repo doesn't make it sacred.

Migrating away from existing standards has been one of the most divisive issues in the Nostr developer community to date. Maintaining backwards compatibility is a massively important principle in software development, whether you're creating a system that's proprietary or an open protocol.

When deploying an update to a proprietary system, it's important that the old version of the application continue to be able to talk to the database, that the old version of the client continue to be able to talk to the backend, etc. But this requirement is ephemeral because the organization running the infrastructure has the ability to eventually upgrade the entire stack and throw away the old code.

In protocol development, backwards compatibility is a much harder problem. In order to fully implement backwards compatibility, you can never really remove a feature. We see this with HTML, where blink and marquee tags created in the 1990s still exist. Programming languages commonly maintain backwards compatibility to make migrations easier - when Python 3 broke compatibility with Python 2, it took almost ten years for users to migrate.

But there is a cost to compatibility: the monotonic increase in implementation complexity. Complexity makes implementation more expensive. This in turn makes the protocol vulnerable to capture by entities with the resources to deal with this complexity.

In a descriptive, lean protocol like Nostr, backwards compatibility remains important (particularly due to the importance of avoiding disruption of network effects), but in a much more practical sense. Backwards compatibility has a purpose, and that purpose is to maintain a good user experience. We don't need to be dogmatic about backwards compatibility. As Ralph Waldo Emerson said, "a foolish consistency is the hobgoblin of little minds."

Backwards incompatible protocol changes aren't as destructive as people frequently make them out to be. This is particularly true because the universal desire for interoperability necessarily encourages conservatism in breaking compatibility.

First of all, the breadth of the nostr protocol makes it possible to change on part of the protocol without affecting the rest. Only the clients which actually implement the feature affected by a change have to care about it. This can be a relatively large number if the feature affected involves follow lists, or microblogging content. But it might be much smaller if it involves some more obscure part of the protocol with only two or three implementations. In contrast, HTML has to be compatible across *billions* of websites.

In addition, there can really be no changes by fiat (even if, as sometimes happens, backwards-incompatible changes make it into a specification document without community buy-in). Nostr is an adversarial environment, and relies on developers to actually implement changes they want to see. To the extent that an implementation has active users, it can choose to go along with the fork, or hold back.

In this way, implementations that want to sponsor either a new protocol feature or an incompatible change can exert pressure on the rest of the network by threatening more or less incompatibility. Likewise, implementations that wish to keep the protocol as is, or not implement a new feature, can do the same. This can be done by shaming competitors in public while maintaining interoperability, or by actually breaking compatibility.

This dynamic is currently playing out with Nostr direct messages. Nostr's original direct messaging implementation (NIP 04) leaks a lot of metadata, which severely undermines user privacy. This problem was severe enough that it led to a new DM standard (NIP 17) which leaks signficantly less metadata. As of the time of this writing, NIP 17 is adopted in the majority of popular Nostr clients, with two significant exceptions - both of which are focused on high quality UX, and so put a premium on DM delivery and product focus.

In a sense, the creation and adoption of NIP 17 DMs can be seen as an attack on these clients because breaking DMs undermines their primary value proposition. The intention behind this "attack" is to protect user privacy but regardless, the introduction of incompatibility forces an eventual resolution to the issue. Eventually, one faction or other will lose users to the other.

One thing to keep in mind, however, is that this kind of adversarial action can cause the protocol itself to lose users, harming all sides. For this reason, backwards incompatibility should be handled with care. Forks always come with the risk of alienating users, or being on the losing end of network effects, which is a natural restraint to reckless behavior.

Forks are a fact of life in the context of an adversarial system. Any actor can choose to fork at any time, for any reason. Even if some forks are well-intentioned and constructive, others may not be. For this reason, implementers must always be prepared to defend their version of the protocol both technically (through defensive coding) and politically (by educating users about the fork and persuading other developers of their view). Core protocol features will gain momentum over time, contributing to stability, but there will always be a certain amount of chaos at the edges. This chaos is a necessary consequence of a radically open protocol.

## Hackability

I've been talking a lot about what interoperability is and how to support it, but I haven't really mentioned what exactly interoperability is for. What good is it for multiple implementations to be able to talk to each other?

This goes back to the problem that Nostr is trying to solve, which is Big Tech's capture of social media platforms and by proxy, their users. In legacy social media, users don't have what's called a credible exit - which is to say that they can't leave a platform and retain their identity or their data.

In order for this to work, not only does data have to be open and unconstrained by custodians (which is what relays and signatures give us) there also have to be multiple implementations that can *interpret* this data. A user has to be able to have a choice; if there's only one implementation because of protocol complexity or propriety, then users don't have the ability to exit because they can't enter something else. In order for users to move, there need to be off-ramps and on-ramps.

Openness makes it possible for multiple implementations to interoperate. But that's a fairly low bar. This is true of (for example) the SQL standard, which defines certain data types, syntax, access control, and a framework for transaction isolation levels, making it possible to access the same database from multiple different software applications. But there are limits to the interoperability this provides; application code remains proprietary. While it's possible to look at a database schema and get a vague sense of what the data is, it's much harder to reverse engineer how it's created or used without looking at the accompanying application.

In the same way, Nostr protocol specifications are only one resource for helping developers create interoperable implementations. This is particularly true because popular features may not necessarily be documented in every case. If a popular implementation isn't open source, it becomes much harder to reverse engineer these protocol features in order to allow others to adopt them. Open-source software function as reference implementations which can be read, copied, and adapted to support new implementations of the same use case. This indirectly benefits users by providing more options to choose from.

But it also benefits users directly. AI coding assistants are bad at a lot of things, but one thing they can do is allow non-technical users to take off-the-shelf software and adapt it to their needs without having to understand what's going on under the hood. Software fails its users more often because of cosmetic problems than because of flaws in the implementation of their problem domain.

A broken click handler can render tens of thousands of lines of well-tested code useless. In the same way, adding a new button to an existing piece of software is often a trivial operation, but requires the expertise of the end user to determine what the button should do. Certain affordance may also only make sense to a single person, and so would never get implemented due to the maintenance cost outweighing the benefit rendered to the single user. Coding assistants enable users to convert rigid, opaque software platforms into environments full of affordances they can take advantage of in the same way an experienced programmer can customize his editor or terminal by writing ad-hoc programs.

Giving end users the ability to create tools for working with the protocol more directly only increases the utility the protocol offers those users. Even if something goes wrong and the AI hallucinates and creates a fork in the protocol, the damage is limited by virtue of the implementation being a one-off - and can easily be reversed by re-prompting. Diversity of implementations also improves the health of the network itself by distributing control over implementations, making the protocol harder to attack.

This dynamic is maybe more important than it sounds at first. I think this is one of the most important things about open protocols and one of the most exciting things about AI-assisted coding. Used properly, AI-assisted coding has the ability to tear down walled gardens at a scale that we can't even imagine.

If AI has the effect of amplifying user agency in the digital world, users become more capable of shaping the digital world based on their values and goals, which are invariably at odds with the software platforms that we're trapped inside in the current iteration of the internet.

Technology doesn't solve problems, people do. Technology is an extension of human will into the world. And yes, there can be unintended consequences. But when individuals use what Ivan Illich calls "convivial tools", their agency is multiplied and the negative externalities are limited to the scale at which that individual operates.

This creates a diverse ecosystem of self-interested actors who can not only do what they want in the digital world, but protect themselves from other people who would take advantage of them, either through massive structures of control or through exploitation of centralized systems by outsiders.

This attitude of creative use of software in order to overcome its limitations or repurpose it for the user's own agenda is encapsulated in the term "hacker". Hackers look at existing software not as complete or normative, but as an opportunity to do something new and subversive. The hacker mindset is the exertion of human agency over technological systems, and is desperately needed in our day of technological passivity.

It could very well be that AI assistance, both in coding and in research and many other ways, is far more important than the existence of an open protocol. It may even obviate the need for protocol documentation to some extent because LLMs can reverse engineer whatever software is already in use. The role of the protocol could shift from a set of rules for how to implement enumerated functionality to a trellis on which organically synthesized human/machine language can grow.

It's also possible that human nature and our willingness to put up with incredible levels of inconvenience will leave this opportunity untapped. The relative lack of adoption even simple things like browser extensions has seen is evidence of our natural inclination to be slaves to our technology. But it's possible AI agents may lead to the spread of something akin to the "hacker mentality" even among non-technical users - not because they make hacking "easy", but by unlocking the universal language of computing for use by non-specialists.

## Application Ecosystems

Given the radical openness of the Nostr protocol, some additional mechanisms are necessary in order to cope with the certainty of running into event kinds that implementations don't recognize. It's categorically impossible for clients to implement support for every Nostr data format because new formats are created constantly. Implementations have to have a strategy for dealing with events they don't understand.

Suppose a user embeds an event to a `kind 30023` long form article in a `kind 1` microblogging post and your client doesn't want to add render support for long form articles. How can you handle that event without knowing what it is?

A few mechanisms have been proposed for dealing with this. They could be more robust, but the foundation has been laid.

First, we have NIP 31, which proposes the inclusion of an `alt` tag on events which describes, in human readable language, what the event is. Following this, a Nostr client could look at a long form article, see an `alt` tag with the title of the article and an explanation of what that event actually is, and display that to the user.

This is something, but it's not very compelling. This is really a dead-end solution, since all the user knows is that they aren't seeing content that they would like to see. There's no call to action for how to actually view the content (unless a link is included in the alt tag - which would be a brittle and centralizing way to handle the problem). Even a simple error message would probably be an improvement over alt messages because at least it would demonstrate to the user that something is indeed missing or broken.

Luckily, we have a better option. NIP 89 defines some mechanisms that can be used by clients for presenting a call to action when faced with unknown event kinds using a technique commonly known in programming as "reflection", which allows a program to inspect its own constructs at runtime and adapt accordingly.

In NIP 89, An "application handler" is a `kind 31990` event which includes tags describing a given application and its purpose, as well as affordances for opening a given event or profile in that application. Application handlers also include a `k` tag, which can be used to filter handler events.

So in our scenario above, the microblogging client might ask the network for `kind 31990` handler events with a `k` tag matching `30023`. This would return a bunch of application handlers with `web`, `android`, `ios`, or other platform tags. The client can then present options for viewing the long form article to the user.

This allows implementations to reduce their scope in order to avoid implementing features they don't care about supporting, while at the same time improving the state of the network by advertising alternatives or complementary applications to their users.

This isn't something that a walled garden would ever want to do. Their impulse is always to vertically integrate either through acquisition or new product development. On Nostr, because implementations can enjoy the network effect of the entire protocol without implementing all of it, developers can afford to recommend alternatives. In fact, doing so makes their value proposition event stronger because users now have a myriad of alternatives to pick from based on their interests, not those of the platform.

NIP 89 further enhances this ability to search for handlers with `kind 31989` "handler recommendation" events. Because anyone can publish a handler event, it's not a good idea to present them to users without some level of vetting. Otherwise it would be trivial to impersonate an existing client in order execute a phishing attack. Even if application handlers are legitimate, knowing whether a given handler is "good" or not is important signal.

`kind 31989` recommendation events allow anyone to advertise clients that they use to handle a particular kind. In combination with web-of-trust analysis, these recommendations can be used by clients to validate a given application handler. Maybe only one person that the user follows uses an application handler, or maybe a hundred people do.

The more popular app is, the more likely it is to provide the user with a good experience. At the same time, the handler with only one recommendation might still be able provide an interesting alternative to the popular app, eroding the hold that popular applications have on the network. This can help mitigate the concentration of power in a few popular implementations.

Application handlers are not the only kind of recommendation event on Nostr by any stretch - recommendation events also exist for relays, Cashu mints, DVMs, and more.

As an aside, one problem with NIP 89 as it currently stands is that handler events have been re-purposed to advertise things other than client-type applications. By way of reminder, Data Vending Machines (DVMs) are service providers that use relays as transport brokers. While these can be thought of as "handling" certain event kinds, the way they do it is very different from how clients work.

Because DVMs have their own reserved kinds this works okay in practice, but would have been much better as an alternative listing event. This migration could be a worthwhile backwards incompatible change to campaign for on the protocol, since it would clear up some confusion about what handling actually means.

For example, if a user wants an application that can "handle" kind `5300` content recommendations, does that mean they want to send those kind of events from a given client? Or do they want to send those events to a particular service provider? This is a good illustration of why it's bad to overload kinds, and why creating new kinds for new use cases is almost always the right choice. And even if DVMs and application handlers were separated, there could still be some ambiguity, for example between publishing a given event kind and rendering it.

The important thing to recognize about recommendation and handler events is that they make possible a social media *ecosystem* incomparable to what has gone before.

In a forest, trees trade sugars to fungi in exchange for minerals extracted from the soil. These wildly different life forms have a mutually beneficial relationship that results from the exchange of these resources. Likewise, Nostr clients and Nostr users benefit from the structured exchange of signed events and functionality.

An "ecosystem" is a complex environment which life forms inhabit. A "media ecosystem" is a complex digital environment that humans inhabit. In this chapter, I have attempted to highlight the benefits of "radical openness" in protocol development. Top-down design reduces essential complexity, making a protocol easier to understand and implement. In contrast, an open protocol multiplies complexity by virtue of the many participants and their relatively free ability to interact with other users and modify implementations.

An increase in complexity makes an environment harder to understand as a whole, but does not necessarily mean a loss of agency. If the appropriate affordances are provided to users to help them manage the complexity they encounter, their agency can be increased rather than diminished. This in turn allows them to determine their own role in the ongoing emergent complexity of the system, and adapt it to their own purposes.

This is a truer form of "social media" than the sanitized, corporate marketing machines which seek to quantify relationships and extract value. If we "embrace the chaos" of the Nostr protocol, it can become much harder to quantify, let alone control, to the benefit of its users.