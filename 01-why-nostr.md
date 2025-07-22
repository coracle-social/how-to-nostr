# Chapter 1: Introduction to Nostr

Nostr stands for "Notes and Other Stuff Transmitted by Relays." It was created as an answer to social media censorship by big tech companies, but has since become much more. Over time, "notes" have become less consequential and the "other stuff" more important.

Nostr is an open protocol, which means anyone can build on it and anyone can extend it. It relies on digital signatures for data authentication and self-hosted or otherwise user-aligned infrastructure for hosting.

The simplest way to think about it is as a Twitter alternative, but one where it's very difficult for any single actor to deplatform users. But in fact, one of the the first content types built for Nostr was related to censorship-resistant e-commerce applications.

Since then, numerous other applications have emerged involving things as broad as media hosting, reviews, chat rooms, calendar events, and even virtual pets.

## Nostr Basics

We'll get into the details later, but let me first sketch out Nostr's technical foundation.

First, users generate and hold a public-private key pair that constitutes their cryptographic identity. They then use this key pair to create digital signatures of content, which is embedded in data structures called "events".

Every event has a "kind," and that kind determines how the event should be interpreted. For example, a kind 3 is a list of people that you follow on social media. A kind 30023 is a blog post. A kind 9 is a chat message, and so on.

Users can also use their key pairs to encrypt or decrypt data, either for themselves or for other people on the protocol.

These events are then transmitted to other people, primarily via "relays," which are simple websocket servers, although they can also be sent by Bluetooth, emailed as attachments, or even written down and sent by carrier pigeon. The relay protocol is very simple, dealing almost exclusively with sending, receiving, rejecting, and requesting events. This makes it possible to create multiple interoperable implementations.

The content types or "kinds" the protocol describes are very loosely coupled, allowing a wide range of applications (or "clients") to be built that can talk to each other. Not every client needs to implement the entire protocol - Nostr is ideal for building small apps that do one thing, and which don't have switching costs.

Here's an example of what this architecture makes possible: Imagine following someone on your microblogging platform of choice, then opening your blog reader and all of their posts are already there. You highlight some text and type a comment. Later, you go back to your microblogging platform and read replies to the comment you made - written by people who follow you from dozens of other apps.

In many ways, Nostr has the potential to be an upgrade to the entire internet. By decoupling data storage (relays), identity (keys), and functionality (clients), it becomes much easier to compose whatever pieces you might need in new and interesting ways. That's a big claim, and there are definitely some things that Nostr can't do well on its own. But it also has adapters that allow third-party services to handle the kinds of computation that Nostr handles poorly.

In terms of the CAP theorem, Nostr has no consistency guarantees, but plenty of availabilityi and partition tolerance. Nostr is essentially a distributed database which allows every node to operate independently without any coordination. By copying the same (signed) data to multiple relays, it will always be available even if some nodes go offline or ban the author.

To recap: Nostr combines cryptographic identities, interoperable data storage, and an open ecosystem of content types to create a system where neither user identity nor user data can be captured by a single entity.

## The Economics of Censorship

I mentioned earlier that Nostr is censorship-resistant. Censorship resistance is a core goal of Nostr because it is in many ways a reaction against the deficiencies of today's internet. Because of how cryptography was adopted primarily by institutions in the early days, the internet is no longer aligned with the interests of its users, but has largely been captured by intermediaries.

As a result, we have a state of rent-seeking in which the users who contribute all the value that the internet has to offer are exploited, undermined, manipulated, deceived, and sold by the custodians of that value.

This is a far cry from the humanitarian dream of the early internet. In the words of Tim Berners-Lee,

> We create the Web, by designing computer protocols and software; this process is completely under our control. We choose what properties we want it to have and not have[...] The goal of the Web is to serve humanity. We build it now so that those who come to it later will be able to create things that we cannot ourselves imagine. [https://www.scientificamerican.com/article/long-live-the-web/]

In contrast, the modern internet is a giant surveillance honeypot. Everywhere you go, you're being tracked - maybe for the purposes of understanding your behavior to serve you ads, maybe for reasons more convoluted, but always in the interest of the ones doing the tracking.

This isn't to say the internet isn't a net positive to those who use it. The internet is the single most successful technology in human history. But it is not what it should be, and reforming it requires active investment from those who stand the gain or lost the most from how it evolves - its users. No one can do this for us - we have to hold companies and platforms accountable ourselves. And in order to do that, we need to understand why censorship happens.

Censorship is not the product of mere arbitrary exercise of power, but of incentives. In authoritarian regimes, censorship is implemented to protect the regime's power. In business, censorship is implemented to protect the business' revenue.

Traditionally, products are sold directly to customers, who then get access to the good or service they've purchased. This business model can transfer to some extent to the realm of information-based products, particularly in a business-to-business setting, where information can be justified in terms of greater productivity.

But consumer software is an entirely different story. If your users are only there to improve their quality of life through access to entertainment or communication, and the marginal cost of production trends toward zero for digital goods, then the price will also trend toward zero because competitors can always offer the same product at a lower price.

Combine that with the imperative for platforms to aggressively acquire users, and you get a strong downward pressure on the upfront pricing of software products. "Network effect" is the idea that a network's value grows proportionally with the number of connections made. A network of 10 people is not worth 10 units of value — it's worth 10 times 10 units, creating an exponential growth curve.

Building a large network requires significant resources in order to fund growth or stay ahead of competitors. These resources, in turn, must be provided by people with capital. As a result, businesses that rely on scaling network effects are typically funded by venture capitalists. This includes social media platforms and similar businesses, such as search engines, marketplaces, and entertainment platforms.

Capitalists want to see the businesses they've invested in make a profit. The best way to make a profit in a market, according to Peter Thiel's *Zero to One*, is to establish a monopoly. Because user retention depends on network effects, market saturation is always the goal, and switching costs must be high. Companies must guard their data jealously to prevent users from leaving.

The art of creating this moat seems to have been perfected. Facebook has been around for a long time, as has Google. In contrast to early internet companies like MySpace, Yahoo, and AOL, these second-generation internet giants have learned how to simultaneously retain and monetize their users.

Very little of these companies' revenue comes from direct monetization. Instead, these big tech companies monetize their users by making them the product. Users have two things that platform owners can sell: their attention and their data. Platforms can only sell these things because they have access to them by virtue of being intermediaries. Platforms subsist by inserting themselves into private or public relationships in order to siphon off these intangible goods.

And it works because individuals don't believe their attention or data are worth anything. Seeing a billboard in your peripheral vision or having cameras record your license plate seem hardly comparable to paying a monthly fee for road use. In the same way, people don't count the cost of their attention or data when accessing the internet.

And it's true, data and attention are not particularly valuable on an individual basis. But they're massively powerful in the aggregate. "Big data" is not mere information, but _the ability to predict patterns of behavior_, which can then be used at scale to manipulate people — to purchase one thing or another, to belive one thing or another, or to act one way or another.

All of this amplifies the more straightforward business model of advertising. Advertising is not just about informing willing buyers about products and services. It's about engineering and conditioning the human mind in order to get it to act in predictable ways.

And so, in a very real sense the cost of giving away our attention and data to these internet intermediaries is the loss of our free will.

## A Path Forward

This didn't have to happen. It's true that everyone wants something for nothing, and so internet users have voluntarily given up their free will to gain connectivity, entertainment, and efficiency. This is a tragedy, but it's also only human nature.

This problem needs to be solved in ways beyond the merely technical - politics, culture, community, and capital all have roles to play here. Nostr's role is to offer tools that individuals can use according to their own values, and for their own interests. Nostr makes it possible for internet users to preserve their own digital sovereignty and hold tech platforms accountable.

My personal hope for Nostr is that it will aid in the restoration and cultivation of human flourishing and agency in a world increasingly mediated by digital technology. Nostr does not solve every problem. The ones it does solve, it often solves poorly. It is not a silver bullet, it is not a panacea. It is a toolset that can be applied to our benefit, or to our detriment.

It is only through people that any of these problems can be solved. Nostr is not a system that will "solve all the problems", but is rather a way of allowing individual agency to be exercised in solving problems germane to their own particular circumstances. In other words, Nostr trusts the user to act in accordance with his own interests.

Like Nostr itself, this book is not a comprehensive guide for how Nostr works or ought to work. It is simply a set of ideas and guidelines for people who wish to create software for themselves or others — software that enriches its users rather than exploiting them.

