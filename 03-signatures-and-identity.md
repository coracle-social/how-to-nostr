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

