# 1. Complex Problems, Simple Solutions

To begin with, I want to present a summary of how the profit motive of internet businesses creates a system of incentives which drives censorship and surveillance capitalism, hurting users and undermining corporations' own value propositions. Next, I'll describe what sort of solution Nostr actually is, and end with quick survey of how Nostr works at a high level — just so we're all on the same page. 

## The Economics of Censorship

Nostr was originally designed to be "censorship-resistant". But this is only one part of a bigger vision. Nostr is designed to *promote the digital freedoms of users* — things like privacy, access to information, anonymity, freedom of association, and [credible exit](https://newsletter.squishy.computer/p/credible-exit). Because of how cryptography was adopted (primarily by institutions) in the early days, the internet is no longer aligned with the interests of its users, but has largely been captured by "platforms".

As a result, we have a state of rent-seeking in which the users who contribute all the value that the internet has to offer are exploited, undermined, manipulated, deceived, and sold by the custodians of that value. This is a far cry from the humanitarian dream of the early internet. [In the words of Tim Berners-Lee](https://www.scientificamerican.com/article/long-live-the-web/),

> We create the Web, by designing computer protocols and software; this process is completely under our control. We choose what properties we want it to have and not have[...] The goal of the Web is to serve humanity. We build it now so that those who come to it later will be able to create things that we cannot ourselves imagine.

In the fifteen years since this was written, the internet has only become more predatory, and proprietary. Everywhere you go, you're being tracked — maybe for the purposes of understanding your behavior to serve you ads, maybe for reasons more convoluted, but always in the interest of the ones doing the tracking.

This isn't to say the internet isn't a net positive to those who use it. The internet is the single most successful technology in human history for promoting access to information, alternative community, and trade. But it is not what it should be. Reforming the internet requires active investment from those who stand the gain or lose the most from how it evolves — its users. No one can do this for us; *we* have to hold companies and platforms accountable ourselves. And in order to do that, we need to understand why censorship happens.

Censorship is not the product of mere arbitrary exercise of power, but of incentives. In authoritarian regimes, censorship is implemented to protect the regime's power. In business, censorship is implemented to protect the business' revenue.

Traditionally, products are sold directly to customers, who then get access to the good or service they've purchased. This business model can transfer to some extent to the realm of information-based products, particularly in a business-to-business setting, where information can be justified in terms of greater productivity.

But consumer software is an entirely different story. If your users are only there to improve their quality of life through access to entertainment or communication, and the marginal cost of production trends toward zero for digital goods, then the price will also trend toward zero because competitors can always offer the same product at a lower price.

Combine that with the imperative for platforms to aggressively acquire users, and you get a strong downward pressure on the upfront pricing of software products. "Network effect" is the idea that a network's value does not grow linearly with the number of users, but quadratically with the number of *connections between users*.

Building a large network requires significant resources in order to fund growth or stay ahead of competitors. These resources in turn must be provided by people with capital. As a result, businesses that rely on scaling network effects are typically funded by investors and oriented at a return on investment. This includes social media platforms and similar businesses, such as search engines, marketplaces, and entertainment platforms.

Capitalists want to see the businesses they've invested in make a profit. The best way to make a profit in a market, according to Peter Thiel's *Zero to One*, is to establish a monopoly. Because user retention depends on network effects, market saturation is always the goal, and switching costs must be high — companies must "capture" their users.

The art of creating this moat seems to have been perfected. Facebook has been around for a long time, as has Google. In contrast to early internet companies like MySpace, Yahoo, and AOL, these second-generation internet giants have learned how to simultaneously retain and monetize their users.

Very little of these companies' revenue comes from direct monetization. Instead, these big tech companies monetize their users by making them the product. Users have two things that platform owners can sell: their attention and their data. Platforms can only sell these things because they have access to them by virtue of being intermediaries. Platforms subsist by inserting themselves into private or public relationships in order to siphon off these intangible goods.

This works because individuals don't believe their attention or data are worth anything. Seeing a billboard in your peripheral vision or having cameras record your license plate seem hardly comparable to paying a monthly fee for road use. In the same way, people don't count the cost of their attention or data when accessing the internet.

And it's true: data and attention are not particularly valuable on an individual basis. But they're massively powerful in the aggregate. "Big data" is not mere information, but *the ability to predict patterns of behavior*, which can then be used at scale to manipulate people — to buy, believe, and act.

Advertising is not just about informing willing buyers about products and services, it's about conditioning people to act in predictable ways. Social engineering (like all engineering) is progressive and totalizing — unless restrained. The cost of giving away our attention and data to these internet intermediaries is, ultimately, the loss of our free will.

## A Path Forward

This slide isn't inevitable. But it's also human nature — everyone wants something for nothing, and so internet users have voluntarily given up their free will to gain connectivity, entertainment, and efficiency.

This problem needs more than a technical solution — politics, culture, community, and capital all have roles to play here. Nostr's role is to offer tools that individuals can use according to their own values, and for their own interests. Nostr makes it possible for internet users to preserve their own digital sovereignty and hold tech platforms accountable.

My personal hope for Nostr is that it will aid in the restoration and cultivation of human flourishing and agency in a world increasingly mediated by digital technology. Nostr does not solve every problem. The ones it does solve, it sometimes solves poorly. Nostr is not a panacea, it is a toolset that can be applied to our benefit or to our detriment, but which has certain intrinsic qualities that the internet desperately needs right now.

I want to emphasize that it is only *through people* that any of the internet's ills can be cured. Nostr is not a comprehensive system for restraining digital evil (such a thing would be itself totalitarian), but a way of allowing individual and community agency to be exercised in solving problems germane to individuals' and communities' own particular circumstances.

## A Simple Protocol

Nostr is in many ways a "dumb" solution to a complex problem. Incentives, structures of power, and technological ecosystems are irreducibly complex, and impossible to understand in detail. But there are key architectural patterns that the modern internet is built on which enable and promote its particular dysfunctions — most importantly, the centrality of servers for both data storage and authentication. 

Instead of using server-based authentication, Nostr leverages cryptography in order reduce the role of servers from powerful hubs to disposable, user-aligned repositories. To join the Nostr network, all a user has to do is unilaterally generate a `secp256k1` cryptographic key pair.

Any number of these cryptographic identities can be used in parallel for whatever purpose — whether to partition user data, create pseudonyms, or to encrypt data. Most importantly, key pairs can be used to create digital signatures of content, which are then embedded in data structures called "events" alongside the user's public key, the event's hash, and some other information.

Once created, events are then transmitted to other people, primarily via "relays," which are simple WebSocket servers, although they can also be sent over Bluetooth, emailed as attachments, or even written down and sent by carrier pigeon. The relay protocol is very simple, dealing almost exclusively with sending, receiving, rejecting, and requesting events. This makes it possible to create multiple interoperable implementations.

The content types (or "kinds") the protocol describes are very loosely coupled, allowing a wide range of applications (or "clients") to be built that can talk to each other. Not every client needs to implement the entire protocol though — Nostr is ideal for building small apps that do one thing, and which don't have switching costs.

Here's an example of what this architecture makes possible: Imagine following someone on your microblogging platform of choice, then opening your blog reader and all of their posts are already there. You highlight some text and type a comment. Later, you go back to your microblogging platform and read replies to the comment you made — written by people who follow you in dozens of other apps.

In many ways, Nostr has the potential to be an upgrade to the entire internet. By decoupling data storage (relays), identity (keys), and functionality (clients), it becomes much easier to compose whatever pieces you might need in new and interesting ways. That's a big claim, and there are definitely some things that Nostr *can't* do well.

In terms of the CAP theorem, Nostr has no consistency guarantees, but plenty of availability and partition tolerance. Nostr is essentially a distributed database which allows every node to operate independently without any coordination. By copying the same (signed) data to multiple relays, it will always be available even if some nodes go offline or ban the author.

To recap: Nostr combines cryptographic identities, interoperable data storage, and an open ecosystem of content types to create a system where neither user identity nor user data can be captured by a single entity. This subverts the central role that servers have in the modern internet, placing users at the center, rather than corporations.