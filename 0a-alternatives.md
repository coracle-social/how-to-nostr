# Alternatives to Nostr

I hope that over the course of this book I have made it clear that Nostr is a unique and compelling solution to the decentralization of social media. But at the same time, it has numerous flaws and trade-offs that make it difficult for developers to use and leave it open to attacks on the protocol.

Nostr is generally optimized not for an ideal solution, but for a good enough solution. In a sense, Nostr trades technical purity for social adoptability, and this may not be the right trade-off.

Right now there is a proliferation of AI-built Nostr applications. In one sense this is great because it allows individual Nostr users to scratch their own itch and to create products for other people. It also means more use cases are served by Nostr's identity and architecture. But at the same time, it saturates the ecosystem with noise, and to the extent that these applications are architecturally flawed, they may actually undermine the decentralization of Nostr.

It's neither easy nor straightforward to implement relay selection heuristics, application handler selection, and web of trust analysis. These things are largely invisible both to developers hoping to accomplish a particular task and users intending to use their solution. But ignoring them results in spam, missing content, and centralization. I hope that the Nostr community can exercise discipline to maintain the integrity of the protocol rather than use it as a way to spin up applications that aren't serious and won't be maintained.

Open source software is not just the publishing of code. It is the commitment on the part of the developer to maintain it, to communicate with the community that forms around it, and the same is true of Nostr. Tragedies of the commons are the natural endpoint for any shared project. We have to care, and we have to act to protect the things that we love.

With that said, I want to enumerate some alternatives to Nostr and describe in brief why I don't see them as viable solutions to decentralizing social media.

## Matrix

First up is Matrix. Matrix is a chat implementation that is federated and encrypted. Matrix has a lot of good things going for it, but suffers from the fatal flaw that your home server is the one that owns your identity. Rather than the holder of the key, Matrix misses out on a lot of the benefits of cryptographic identity.

As a result, Matrix's protocol is also far more limited to chat applications. It doesn't have the rich content types that Nostr has, or the decentralized permissionless ability to create new ones. Matrix as an ecosystem is far less open, and the architecture is more permissioned. The same criticism goes for Mastodon. If your home server in either system deplatforms you, you lose your identity. Data is not signed and so it can't be re-uploaded.

Both systems are the application of the centralized platform model to a decentralized platform model. But the administrators of these platforms are no less kings, and in some ways are more so. Large companies have to follow the law and be very responsible and sensitive to the effect their actions have on their reputation. The despot of a Mastodon server has far less accountability to their users.

Small servers are also far less stable and might disappear for any number of reasons other than deplatforming. To be sovereign or to have sovereign identity on Mastodon is to run your own home server, which is not something most people are willing to undertake.

## Scuttlebutt

Second is Scuttlebutt. I've mentioned before that Scuttlebutt is the inspiration for Nostr in a lot of ways. Scuttlebutt has one main flaw, which is that user content is linked, which means in order to validate the most recent event by a particular key, you have to download all of that user's data. This doesn't scale to a larger social network.

Another problem with Scuttlebutt is that keys can't be used for multiple applications at the same time for the same reason. If there was a race condition and different pieces of content were signed at the same time by the same key, that would result in a fork and one of the messages would be dropped. This could be solved in many ways, but in practice it has encouraged its users to use a separate identity for each device, which means that you can't be followed as an individual. You have to be followed as a collection of keys.

Nostr is inspired by and builds on Scuttlebutt's successes.

## Pubkey

Next, why not Pubkey? Pubkey is a social protocol created by John Carvalho, which uses cryptographic identity and home servers.

There are two parts to Pubkey. First, they use user cryptographic identities to create and maintain entries on the mainline DHT in order to route requests to the correct server. The mainline DHT is the most used DHT in existence and is highly Sybil-resistant, which makes it a much better index than Nostr relays can provide. On Nostr, indexes are simply relays that store a particular kind of event.

This works okay, but this is an area that we can borrow from Pubkey in order to improve the resilience of Nostr bootstrapping. Unfortunately, mainline requires the use of a different curve, and so a different DHT will need to be used or Nostr keys will have to be adapted to whatever curve mainline uses.

The second half of Pubkey is home servers, which have the same problems that Mastodon and Matrix home servers do. Except that they can't deplatform your identity because your identity is cryptographic. But all of your content is stored on Pubkey home servers, which are either self-hosted in the best case, or rented from a server provider. For most people, servers are going to be rented by a provider and because home servers are single rather than plural, there's no redundant data storage. And if there were, Pubkey doesn't, by default, sign data, which means data authentication is not decoupled from data storage. And so replicating data across the network is not possible.

## Blue Sky

Next up, Blue Sky. Blue Sky was intended to be something very like Nostr. And on paper it is. The architecture is sophisticated, and certain problems are addressed that Nostr doesn't address like human readable names, although these are of course subject to the limitations of Zooko's triangle.

But in practice, Blue Sky requires infrastructure providers to host all data on the network. This is complicated because there are different data storage services, but the service that responds to user queries has to have access to, has to have a copy of all the data on the network.

As a result, Blue Sky's infrastructure is too expensive to be run by individuals or smaller entities, resulting in a few centralized service providers. Because of this, Blue Sky is expensive to run and is able and required to implement a number of censorship policies, including collecting KYC information from users. [I'll have to fact check that.]

Blue Sky seems to be turning out to be the same kind of next generation monolithic social media platform with all the same problems and a more sophisticated architecture.

## What Makes Nostr Different

In contrast to all these alternatives, Nostr is the only one that provides cryptographic identity, service discovery, content replication through signed data, low barrier to entry for service providers, and network partitioning.

This last one is particularly interesting because it requires the adoption of a different paradigm than we've been led to accept on legacy social media. The idea of a global view of the internet is not coherent, but has been simulated by services like Google providing search and walled garden social networks which provide a global view of all their members. But in neither case is there really a global view. There are parts of the internet that are out of reach of Google, behind authenticated servers or on the dark web. The same way there's information that is out of Twitter's reach because it's not on their platform—it's on someone else's.

Nostr admits the fact of this limitation of knowledge. There is no global view of human knowledge. Knowledge networks are necessarily partitioned. Society is necessarily partitioned. Nostr embraces that partitioning. Through interoperability and signed data and cryptographic identity, everything on Nostr is portable from one social cluster or network cluster to another.

And I think more than relays or signed data, this is the thing that makes Nostr special. It is a social network that reflects the social dynamics of the real world more faithfully than the alternatives.

## Why Not Start Over?

Now why not the next thing? Nostr could be improved. It has numerous cosmetic design flaws, relies on aggressive synchronization in order to avoid race conditions, a number of NIPs overload kinds and tags, bootstrapping is a convoluted process, and incompatibilities between clients are common.

Instead of having a single reference implementation that's used by all clients, Nostr has dozens of separate SDKs. And so incompatibilities and differences in paradigm and nomenclature go all the way down to the bottom. I've talked some about how this is a feature rather than a bug, but it also makes for a far more chaotic ecosystem.

What if we started from scratch with Nostr? We could have a single reference implementation and sophisticated design decisions like binary protocols or CRDTs. Such a project could do good work.

But Nostr is more than a technical specification. It is a community. The ability to hack on Nostr is part of what makes it special. The different existing applications are what make it real. None of them are perfect, and many of them will disappear over time. But with Nostr, we have something. Whereas with a successor protocol, we have nothing.

That situation could change. But it's possible to make the perfect the enemy of the good. If Nostr is good enough—which is a big if—then abandoning it would be to reset the clock on several years of development.

People have been developing decentralized protocols for as long as I've been alive. Over and over they get captured. Maybe the destiny of Nostr is to get captured, but to provide a brief respite for its users from the control and oversight of governments and corporations.

Nostr doesn't have to live forever in order to succeed. And Nostr doesn't have to be used by the whole world in order to provide value. It's already providing value to the 100,000+ users that use it every day.

I would like to see more adoption and I would like to see a better technical foundation, but we can't have all that we want. Part of building a commons is compromise. Not only with one another, but with reality as we find it.

Nostr is nothing but compromise. For that reason, I want to end this book by encouraging you and every developer who builds on Nostr to embrace compromise, not withdraw from the difficult work of coordination and collaboration, but to embrace the politics inherent in protocol design. Again, not in a bureaucratic sense, but in the sense Aristotle meant.

The city is a place in which a community of people live, whose lives in turn build and rebuild the city. A digital commons is a digital space in which people live and by their activity, build and rebuild that commons.