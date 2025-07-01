# Custody and Cryptography

Now that we've gotten some of the boring stuff out of the way, we can get into some of the meat of what makes Nostr special. While Nostr makes things marginally more exciting by virtue of its design choices, data modeling is common to pretty much every form of software. What isn't as commonplace is Nostr's use of cryptography.

Nostr is built on the same elliptic curve that Bitcoin is built on: secp256k1, which is based in turn on elliptic curve Diffie-Hellman, or ECDH. Diffie-Hellman is a technique that's been around for a long time and enables all kinds of things, from digital signatures, to encryption, to secret sharing, and even distributed signature schemes. This won't be a thorough explanation of what all we might be able to accomplish with ECDH, just a primer on how Nostr uses it and why it matters.

For starters, digital signatures in particular are essential to making Nostr work. The goal of Nostr is to break down walled gardens by subverting one of their key value propositions: content authentication. Or, in other words, the ability to know that a particular person said a particular thing.

This is a challenge in the digital world because information can be copied or fabricated at will. Simply saying that someone authored a particular piece of content doesn't make it so. When you go to Twitter and you load up a tweet, you only know that tweet is real and was actually created by the person that Twitter says it was created by because you trust Twitter. If you don't trust Twitter, you can't know if it is real or forged. And if someone takes a screenshot of that or copies the text and emails it to you, then you have even less assurance that what's been presented to you is actually authentic.

What this means is that data that is not cryptographically signed is tightly coupled to custody. The only person who can reliably attest to the authenticity of a given piece of information is the person who can trace its provenance from the author, through storage, and to your device. This is very convenient for social media platforms - reliance on unsigned data means that they are needed. There has to be a single trustworthy custodian in order for unsigned data to work. The same is true of search results on Google; you don't know that search results are any good unless Google says they are.

What signed data gives us is the ability to know that something is true without having to trust anyone. (This is also true of zero-knowledge proofs, or ZKPs, which allow the result of an arbitrary computation to be proved without revealing certain information. ZKPs are outside the scope of this document, but are common in cryptocurrency applications, and could be applied in interesting ways to nostr.)

If I create a note on Nostr, I use my private key to sign it, which allows anyone else to verify the result against the hash of the event and my public key (which is attached to the event). This lets them know that the event was created by the person who has access to my private key, A.K.A., me.

What this means is that I can take a Nostr event and send it over an untrusted channel without the person reading it losing the ability to know that it was me who said it. As long as they know my public key, I can email a Nostr event, I can send a Nostr event over a peer-to-peer communication or over Bluetooth or over the LAN, or I can print it up and send it by mail.

This verifiability is one of two primary design goals listed in the seminal 1977 RSA paper (the other being privacy):

> The era of “electronic mail” may soon be upon us; we must ensure that two important properties of the current “paper mail” system are preserved: (a) messages are private, and (b) messages can be signed. We demonstrate in this paper how to build these capabilities into an electronic mail system.

# Publicity Technology

I'll hold off on discussing encryption until another chapter. For now I want to focus on what signed data (and by extension cryptographic identity) gets us, and how best to use it.

The current business model that fuels social media platforms is predicated on the capture of user data for their exclusive monetization. The user has become the product. Our data is used in a focused way to create targeted advertisements, or in the aggregate to understand and anticipate user behavior.

Signed data solves half of that problem. Assuming that signed data is not kept private and is publicly available, it actually worsens the data analysis problem by making all activity public and accessible to anyone who wants to analyze it for patterns and manipulate people in the aggregate. This is a weakness of Nostr that should not be neglected - Nostr is not privacy technology (at least, not by default).

Nostr is publicity technology. When you create an event and you send it to untrusted custodians with no access controls or encryption layered on top, you are advertising something about yourself to the entire world. All the data included in an event and all the metadata that can be harvested by observers and middlemen points back to you and tells them something about you.

This is perfectly acceptable for Twitter clone use cases, but has to be considered when building products on Nostr that require a higher level of user privacy. For this reason, it's best to use a VPN and Tor in combination with Nostr if you're concerned about privacy. Even so, in the aggregate this data can still be collected and used to understand both individual users and entire social clusters.

With that caveat out of the way, signed data does solve the other half of the problem, which is the capture of user attention through intermedation. The current business model of social media platforms is predicated on the attention users give the platform, which is maximized by designs which stimulate engagement. To define my terms, "engagement" is the consumption and creation of digital content.

The old way of doing this was through centralized content production. A business would create content - for example, movies, magazines, or podcasts - and present it to users for their consumption. Of course, it was a lot easier to directly monetize this content because it was both high quality and protected by intellectual property laws. On social media, content is not produced by the platform, but by users. This introduces a second side to engagement - users not only consume, but also produce content, which keeps them even more engaged, and provides even more information about them to the platform.

When content is signed, it can no longer be captured by the platform. The result is that platforms lose the ability to enforce their monopoly on user attention. As a result of signed data, user attention can be diverted to other platforms that host a copy of the data. Nostr takes this effect even further by decoupling data storage and user interaction - relays store notes, but clients mediate user interactions.

On Nostr, clients can be more aligned with users, since they can only capture user attention to the extent that their _functionality_ is what's valuable to the user, not the _data_ they have access to.

The ability users have on an open network to leave a platform without losing all their data or their social graph is called "credible exit". This is the opposite of "vendor lock-in," which occurs when platforms make it difficult to leave them. If you've logged 15 years of activity on Facebook, it's very hard to leave Facebook - the export feature Facebook offers is nearly useless because it breaks all the links in your social graph. But if all your Facebook data was signed and the social graph was open, it would be very easy to leave.

Social media companies can still exist in the world of signed data, but they will have to offer a real value proposition to their users in order to retain them. This means that they'll be more likely to serve their users rather than extract as much value as possible from them.

Whether open source software wins out, or for-profit companies start building on Nostr, signed data weakens platforms' hold on their users and realigns the interests of social media with users. And while I think there's still room for skepticism about the effects of social media in general, this corrects a lot of perverse incentives that currently exist in the system.

# Your Very Own Number

Very closely related to the idea of signed data is that of cryptographic identity. On almost every digital platform in existence, identities are the property of the platform, not of the user. In most cases, a user identity is not actually the user's email, phone number, or a username, but a numeric ID or UUID that's stored in a database. This number is generated by the platform when a user registers, and belongs to it. The platform can change this number, redefine it, give it away, or delete it at any time and with impunity.

The internet of today is entirely occupied by renters. Users go from one place, from one website or app to another, asking the owner of that property if they can *please* check their messages, post a meme, express an opinion, or buy something. Users have next to no leverage to force their way in to the vault that holds their data. Content creators are frequently deplatformed. Community groups are banned. Even websites are frequently taken down.

This is even more insidiously evident with social sign-on. When a website integrates Facebook or Google social sign-on, not only does the identity provider get the ability to track your movements across the internet, but they also get the ability to revoke your access to these third party services at any time! Even if you don't use social sign on, your email provider probably has the same ability to revoke your access from the rest of the internet. This over-reliance on identity providers leaves users extremely dependent and vulnerable.

An "account" is simply an entry in a database that associates some asset with a person or an entity. The user is the entity, and the custodian holds the asset. Whether you're signing in to Netflix, sharing your PPI with your bank teller, or swiping your keycard to get into work, the credentials you present are *issued* to you by the service or an authority they trust (yes, even your birth date, which is only meaningful because it's printed on your ID).

Cryptographic identity turns this on its head, because instead of being granted an identity by a platform, you provide your own user ID. And because you don't have to tell anyone your secret in order to prove you own it, you have exclusive access to your identity.

Secret keys can also be generated out of thin air, giving you as many identities as you need. This allows you to re-use an identity as much or as little as you need, depending on whether you're looking for privacy or convenience in any given case. Using the same key for your social media profile as well as for your wallet makes it easy to pay friends - but might also link your payment history to your public persona.

This of course requires users to be responsible and understand the privacy trade-offs of reusing their keys, just like it requires users to know not to reuse their passwords. But the key point here is that user experience and education can be layered on top of this primitive in a way that can't be layered on top of custodial account access. Cryptographic identities allow users to be exclusively and finally in charge of their identity.

# Agency and Identity

Cryptographic identities attack walled gardens from multiple directions at once. Because data is signed and verifiable, platforms are no longer necessary for tracing the provenance of a given message or social media post. The flipside of this is that platforms are no longer able to act on the behalf of their users with impunity. If data is expected to be signed and users hold their own keys, user activity can no longer be forged. This is important in cases where action is required in order to deplatform someone - for example, when moving money out of a bank account.

Cryptographic identities are more private than claims that are shared with custodians. When you sign in with a username and password, that goes into a database that may be the target of leaks or hacks. If it's valuable, this data almost always ends up on the dark web.

In contrast, when using asymmetric key pairs the only thing that can leak from the third party database is your public key, since your private key never leaves your own device. Of course there's a whole art to keeping your private key safe, which we'll get into later. But even without sophisticated key management cryptographic identities drastically decrease users' vulnerability to identity theft and phishing attacks.

--- raw


Identity is not the end of the story though, because from it stems all kinds of implications having to do with connected identities in a system where cryptographic identities can not only protect data but also be referenced elsewhere. It becomes possible to form connections between these disconnected identities simply by referencing another user's public key in a given context. An obvious example of this is mentioning someone in a microblogging application. That person can then be notified that someone was talking about them. They can open up that tweet in their client of choice and view and reply as the spirit moves them.

Likewise, direct messages become possible between cryptographic non-custodial identities. Likewise, payments. Nostr's Zaps are addressed to another person's public key.

Nostr has lists of people, follow starter packs, and follow lists. And then of course there are the implicit connections where if someone reacts positively to a certain person's notes over and over again over time, even if that person isn't explicitly referencing, even if they're not following that person, that can be seen as an implicit endorsement of that person's entire identity. Weak, but it is signal. And this is where the data analysis problems of centralized social media and the risks associated with public and open social media rebound to the user's benefit once again.

Through simplistic analysis of follow graphs or more sophisticated analysis of explicit and implicit Web of Trust connections, identities can have reputation associated with them. Reputation that is relative to your vantage point in the network.

In concrete terms, if you follow someone, then that person is explicitly trusted by you, at least in whatever terms "follow" means. It doesn't mean that you endorse their views, or that you would trust them to watch your kids, but it is nothing more or less than a follow.

Well, that person also follows people on the network. And so, by virtue of that one connection that you explicitly made, many more weaker connections are implied. And this allows you to traverse the network in order to reach parts of it that you aren't explicitly aware of.

As mentioned above, other types of connections can be brought into this graph analysis for any number of purposes. For example, Coracle's Web of Trust is simple. It calculates a score, which is the number of people who you follow who follow a given person minus the number of people you follow who mute that person, which allows for negative weight connections to be established. Meanwhile, Vertex is a service that calculates much more sophisticated, PageRank-style web of trust scores. The trade-off between these is that this follow graph calculation can get really heavy really fast. Coracle only scores things with a single hop or with two hops, whereas other algorithms may go to three or four or even six degrees of Kevin Bacon and incorporate other metrics as well.

There is a school of thought that would seek to extend these implicit or weak attestations with much more explicit, strong and potentially annotated attestations. For example, "I trust this particular person at a level of seven to recommend movies."

There are indeed contexts where you might want something like that. For example, a Goodreads alternative. But in most cases, creating the data required to build these sophisticated granular webs of trust is difficult to incentivize users to create, especially when it reveals so much about themselves.

And so Web of Trust is valuable less for embodying real world trust in a digital setting than for embodying digital trust, which is in most cases a very different thing. Digital trust is concerned with issues related to spam or ideology or entertainment value, which are a fairly low bar and can be used effectively to prevent spam or harassment or illegal content, but which aren't good for choosing peers in a financial transaction.

There are, for example, efforts to rate relays or ecash mints by taking advantage of the social graph. But the effectiveness of such reviews is very nuanced. For example, if an ecash mint has a large number of high reviews, that means next to nothing about how trustworthy the mint actually is, only that it hasn't rugged users yet. Odds are the mint has gained this reputation based on low latency, high availability, or good customer service.

This is the problem with reviews in general. A buyer who's already transacted has a much lower stake in the review process than someone who has not yet completed the transaction. But Web of Trust does go some way towards solving the abuse of reviews that's so prevalent on Amazon and other shopping sites, where platforms are essentially Sybil attacked because they don't have a vantage point from which to assess the reputation of any given reviewer. Instead, companies that want to market their products spin up a number of fake accounts and leave high ratings with bogus reviews just to get cheap products promoted and crowd out more organic small scale options.

As I mentioned before, Web of Trust isn't a single thing. There are simple, straightforward algorithms and there are more complex ones, more and less effective ones. But Web of Trust doesn't have to be strictly trust or even social signals. Nostr has a few other affordances that can be used to supplement the trust graph. For example, NIP-05 registration. If a user has a NIP-05 address that's issued by a highly reputable address service, then perhaps they can be trusted despite having no social signal. Similarly, a public key that begins with several zeros demonstrates that a certain amount of work was put into generating the key. NIP-13 also allows for proof of work generation on an event by event basis. Proof of work on its own is definitely not a panacea, but it can make spam slightly more expensive and can be combined with Web of Trust for a more robust trust profile.

This is important for users who are new to the network and don't yet have any attestations from other users about the authenticity or value of their activity. In other words, if no one has ever tweeted, how do you know whether to show their post? How do you know whether to show someone's post if they've never received any interaction from anyone before?

When bootstrapping the network, when bootstrapping your personal network, new users are often left out in the cold. So the door does have to be left open a crack for these new users without allowing spammers and bad actors to flood in.

Now, all of these things are predicated on users being able to securely and conveniently hold their private key, which is a big assumption. Over a decade of research has gone into building key storage solutions for Bitcoin wallets and the trade-offs involved in those design decisions. Nostr is just as complicated.

The stakes are slightly different. Whereas with Bitcoin, you can lose real money. On Nostr, you can lose your social identity. It's honestly hard to know which one would be more destructive—it depends on who you are and what you use social media for, and how much money you have.

Nostr also has some disadvantages in comparison with Bitcoin. With Bitcoin you can rotate keys by simply sending funds to a new address and throwing away the old address. On Nostr, your identity is your public key. And so if your key is lost, well, on Bitcoin you can't do anything anyway if your key's lost. But on Nostr, if your key is compromised or in danger of being compromised, there's not really anything you can do.

Key rotation is something that we have to figure out on Nostr if Nostr is going to succeed. There have been some proposals, but none of them have gained enough traction to be implemented. So it remains an open question. However, there are a lot of things we can do to make key storage safer and more convenient.

A number of different signer protocols have been experimented with, including NIP-07 browser signer extensions, NIP-55 Android Intent-based signers, and NIP-46 remote signers.

In my opinion, NIP-46 is the most universally available of these options and also provides for the best user experience. Well, its user experience isn't quite as simple as it is for NIP-07 or NIP-55, unless you take into account that neither of those options works remotely and both require the user to install something, an additional application before they start using Nostr, which is an insane amount of friction to impose.

NIP-46 on the other hand works anywhere from anywhere. You can install your signer application on your phone, on your desktop, or in the cloud, put your key there or have it generate a new one and move forward. Particularly promising are multi-signature bunkers, which allow for the selection of multiple unrelated custodians, each of whom has only a fraction of your whole private key, which means that unless they collude, your key is safe. Of course that's a big assumption and so the correct custodians have to be chosen, and for new users who aren't going to have familiarity with the ecosystem they're inevitably going to offload their selection to the application through which they're signing up.

The same risks apply to custodial signers that apply to ecash mints. But with some care, a combination of manual selection on the part of the application developer and Web of Trust based heuristics can be used to choose unrelated, trustworthy custodians for new users.

A common signature scheme for new users is two of three, where two shards of the key are required in order to sign an event. But this threshold could be increased to three of five or four of five or even more, and the user could hold one of the shards themselves in the application.

Another good pattern for onboarding users to keys is sending the user an email with an encrypted version of their private key. The user can provide a password which can then be used to encrypt the private key and they can receive that opaque version, forget about it, and then retrieve it later when they need it. This is great because users are not going to set up proper key storage the first time they try a new social media application. Deferring the learning process until they have a stake in the network is going to see a much higher rate of success.

Other patterns that are common that I don't think should be used on Nostr include seed words. Seed words are great for securing Bitcoin in cold storage because cold storage requires manual entry. A 64-character hex key is going to be a lot harder to enter than 12 or 24 words, especially if you're engraving the characters on steel.

But on Nostr, cold storage is just not necessary, except in the most exceptional of cases. On Nostr, keys need to be hot because they need to be able to sign things frequently. Otherwise you're constantly entering your seed words. Seed words are basically useless for storing Nostr keys. Just put your key in a password manager. If you're really paranoid, encrypt it and then put it in your password manager.

But your key is going to be on your signing device wherever that is and that signing device is going to be connected to the internet. This is another reason that multi-sig is worth investing in. Even if you're not using custodians to hold your keys, you can get a lot of benefit out of multi-sig by placing shards of your key on different devices. That way if a single device is compromised, that shard can be revoked and you can rotate your signer setup without rotating your key.
