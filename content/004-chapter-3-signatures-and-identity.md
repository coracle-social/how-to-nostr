# Chapter 3: Signatures and Identity

Now that we've gotten some of the boring stuff out of the way, we can get into some of the meat of what makes Nostr special. While Nostr makes things marginally more exciting by virtue of its design choices, data modeling is common to pretty much every form of software. What isn't as commonplace is Nostr's use of cryptography.

Nostr is built on the same elliptic curve that Bitcoin is built on: secp256k1. Asymmetric cryptography enables all kinds of neat things from digital signatures, to encryption, to secret sharing, and even distributed signature schemes. This chapter isn't a complete catalog of what we might be able to accomplish with it, but will instead focus on how Nostr uses it and why it matters.

## Information Wants to Be Free

Digital signatures are essential to making Nostr work. The goal of Nostr is to break down walled gardens by subverting one of their key value propositions: content authentication. Or, in other words, the ability to know that a particular person said a particular thing.

This is a challenge in the digital world because information can be copied or fabricated at will. Simply saying that someone authored a particular piece of content doesn't make it so. When you go to Twitter and you load up a tweet, you only know that tweet is real because you trust Twitter. And if someone takes a screenshot of that or copies the text and emails it to you, then you have even less assurance that what's been presented to you is authentic.

What this means is that data that is not cryptographically signed is tightly coupled to custody. The only person who can reliably attest to the authenticity of a given piece of information is the person who can trace its provenance from the author, through storage, and to your device. This is very convenient for social media platforms — reliance on unsigned data means that they are needed. There has to be a single trustworthy custodian in order for unsigned data to work. The same is true of search results on Google; you don't know that search results are any good unless Google says they are.

What signed data gives us is the ability to know that something is true without having to trust anyone. If I create a note on Nostr and use my private key to sign it, anyone can verify the signature using the hash of the event and my public key (which is attached to the event). This lets them know that the event was created by the person who has access to my private key, i.e., me.

A Nostr event can thus be sent over an untrusted communication channel without the recipient losing the ability to know that it was me who signed it. As long as they know my public key, I can email a Nostr event, I can send a Nostr event over a peer-to-peer communication or over Bluetooth or over the LAN, or I can print it up and send it by mail. No intermediary can stop me without securing a monopoly on my communication.

## Publicity Technology

The business model that fuels today's social media platforms is predicated on the capture of user data for their exclusive monetization. The user has become the product. Our data is used in a focused way to create targeted advertisements, or in the aggregate to understand and anticipate user behavior.

Signed data solves only half of this problem — it actually *worsens* the problem to the extent that data is public and accessible to anyone who wants to analyze it for patterns. Designing digital identity also has an incredible amount of complexity involved, and must be approached with caution. From Philip Sheldrake's essay, [Human identity: the number one challenge in computer science](https://generative-identity.org/human-identity-the-number-one-challenge-in-computer-science/):

> Put starkly, many millions of people have been excluded, persecuted, and murdered with the assistance of prior identity architectures, and no other facet of information technology smashes into the human condition in quite the same way as digital identity[...] This should give anyone involved in digital identity cause to consider the emergent (i.e. unplanned) consequences of their work.

When designing systems that make use of digital identity, it's important to work from a conception of identity not as *objective*, but as *subjective* — that is, defined not by a set of static attributes, but by the dialectical contexts and relationships the person behind the identity participates in. The former kind of identity allows others to *act upon* the identity; the latter allows the person who own the identity *to act.*

Cryptographic identity doesn't automatically make this distinction, but can be used in either way. If the goal is user empowerment, a system of identity that is crafted to protect the digital freedoms of the user must be carefully designed.

Because identity is intended to be shared in a social setting, Nostr is not really "privacy technology". Rather, Nostr is "publicity technology".

When you create an event and you send it to untrusted custodians (particularly if left unprotected by access controls or encryption) you are advertising something about yourself to the entire world. All the data included in an event and all the metadata that can be harvested by observers and middlemen points back to you.

This is suitable for Twitter-like use cases (although user privacy is a concern even in a broadcast social media context), but always has to be considered when building products on Nostr. For users, it's best to use a VPN and Tor in combination with Nostr if you're concerned about privacy. Even so, in the aggregate signed data can still be collected and used to understand both individual users and entire social clusters.

## Dis-intermediating Data

With that in mind, signed data does help reduce the capture of user attention by dis-intermediating content delivery. The current business model of social media platforms is predicated on the attention users give the platform, which is maximized by designs which stimulate "engagement", the creation and consumption of digital content.

The old way of doing this was through centralized content production. A business would create content — for example, movies, magazines, or podcasts — and present it to users for their consumption. Of course, it was a lot easier to directly monetize this content because it was both high quality and protected by intellectual property laws.

On social media, content is not produced by the platform, but by users. This introduces a second side to engagement — users not only consume, but also produce content. This keeps them even more engaged, and provides even more information about them to the platform.

When content is signed, it can no longer be captured by the platform (even if it is still visible to the platform). The result is that platforms lose the ability to enforce their monopoly on user attention. As a result of signed data, user attention can be diverted to other platforms that host a copy of the data. Nostr takes this effect even further by decoupling data storage and user interaction — relays store notes, but clients mediate user interactions.

On Nostr, clients can be more aligned with users, since they can only capture user attention to the extent that their *functionality* is what's valuable to the user, not the *data* they have access to.

The ability users have on an open network to leave a platform without losing all their data or their social graph is called [credible exit](https://newsletter.squishy.computer/p/credible-exit). This is the opposite of "vendor lock-in", which occurs when platforms make it difficult to leave them. The export features social platforms offer are nearly useless because they break all the links in your social graph. But if all your social data was signed and the social graph was open, it would be quite easy to leave.

Social media companies can still exist in a world of signed data, but they will have to offer a real value proposition to their users in order to retain them. This means that they'll be more likely to serve their users rather than extract as much value as possible from them.

Whether open source software wins out or for-profit companies start building on Nostr, signed data weakens platforms' hold on their users and realigns the interests of social media platforms with those of their users. And while I think there's still room for skepticism about the effects of social media in general on people and communities, removing lock-in fixes a lot of existing perverse incentives in the system.

## Your Very Own Number

On almost every digital platform in existence, identities are the property of the platform, not of the user. In most cases, a user identity is not actually the user's email, phone number, or a username, but an ID that's stored in a database. This number is generated by the platform when a user registers, and belongs to the platform, which can change this number, redefine it, give it away, or delete it at any time and with impunity.

The internet of today is entirely occupied by renters. Users move from one website or app to another, asking the owner of that digital estate if they can *please* check their messages, post a meme, express an opinion, or buy something. Users have next to no leverage to force their way in to the vault that holds their data. Content creators are frequently de-platformed. Community groups are banned. Even websites are frequently taken down.

Even worse, when a website integrates social sign-on (to make life easier for the user of course), not only does the identity provider get the ability to track your movements across the internet, but they also get the ability to revoke your access to these third party services! Even if you don't use social sign on, your email provider probably has the same ability to revoke your access from the rest of the internet. This over-reliance on identity providers leaves users extremely dependent and vulnerable.

An "account" is simply an entry in a database that associates some asset with a person or an entity. The user is the entity, and the custodian holds the asset. Whether you're signing in to Netflix, sharing your PPI with your bank teller, or swiping your keycard to get into work, the credentials you present are *issued* to you by the service or an authority they trust (yes, even your birth date, which is only meaningful because it's printed on your ID).

Cryptographic identity turns this on its head, because instead of being granted an identity by a platform, you provide your own user ID. And because you don't have to tell anyone your private key in order to prove you own it (in contrast with, say, social security numbers), *you* have exclusive access to your identity.

Secret keys can also be generated out of thin air, giving you as many identities as you need. This allows you to re-use an identity as much or as little as you need, depending on whether you're looking for privacy or convenience in any given case. For example, using the same key for your social media profile as well as for your wallet makes it easy to pay friends — but might also link your payment history to your public persona.

This of course requires users to be responsible and understand the privacy trade-offs of reusing their keys, just like it requires users to know not to reuse their passwords. But user education is a tractable problem, while digital freedom is impossible without cryptographic identities. Users can be exclusively and finally in control of their identity.

## Agency and Identity

Cryptographic identities attack walled gardens from multiple directions at once. Because data is signed and verifiable, platforms are no longer necessary for tracing the provenance of a given message or social media post.

The flip side of this is that platforms are no longer able to act on behalf of their users with impunity. If data is expected to be signed and users hold their own keys, user activity can no longer be forged. This is important in cases where action is required in order to de-platform someone — bank accounts can be frozen, but bitcoin wallets are held in alodium.

Cryptographic identities are more private than claims that are shared with custodians. When you sign in with a username and password, that goes into a database that may be the target of leaks or hacks. If it's valuable, this data almost always ends up on the dark web.

In contrast, when using asymmetric key pairs the only thing that can leak from the third party database is your public key, since your private key never leaves your possession. Of course there's a whole art to keeping your private key safe, which we'll get into later. But even without sophisticated key management, cryptographic identities drastically decrease users' vulnerability to identity theft and phishing attacks.

## Identity Webs

Identity *a la carte* is not the end of the story though. Cryptographic identities can free data from custodians, but they can also be referenced *by* that data, making it possible to assign meaning to identities themselves. A simple example of this is a "mention", which allows someone to be notified about a conversation and engage with it. The same goes for direct messages, payments, friends, follows, and more. Since each reference of a public key is also signed, relationships between keys can begin to form. This is known informally as "webs of trust", although the word "trust" might overstate how reliable these connections are. A better term might be "identity webs".

The semantics of connections between identities may be more or less explicit (a social media "follow" is a pretty well-defined concept, while a comment on a blog post carries far less meaning), but every connection has significance. In the aggregate, the same types of analysis that threaten user privacy (as mentioned above) can be leveraged to benefit users who voluntarily produce content for public consumption.

Whether through simplistic analysis of follow graphs or sophisticated analysis that scores transitive relationships or different types of interactions, reputation can be assigned to identities. We often think of "reputation" in objective terms, but in reality it's entirely relative to the values and network of the person assessing reputation.

In concrete terms, if you follow someone you're expressing a non-zero amount of "trust" in that person. It doesn't mean that you endorse their views or that you would trust them to watch your kids, but it does indicate that they're of interest to you in some way. Other people can then borrow this attestation to augment their own ability to assess reputations, expanding their ability to traverse the network. However, with each connection the ability to assess reputation diminishes since trust is increasingly delegated.

For this reason, reputation has to be calculated from a trusted starting point and only via trusted connections, or else it becomes subject to sybil attack. If reputations are not calculated conservatively, it can become trivially easy for sock-puppet accounts to infiltrate a network. In other words, if you calculate reputation starting from the perspective of a scammer, you're going to have scammy scores. Likewise, if you over-weight weak attestations (for example, ambiguous emoji reactions), it's unlikely you're going to get good results. Garbage in, garbage out.

This conservatism naturally results in network partitioning, in which someone from one social cluster might find it difficult to establish the reputation of someone in a different social cluster. There are "global" algorithms like PageRank (named after Google's Larry Page) which attempt to circumvent this constraint, but are inherently vulnerable to sybil attack.

One solution to this problem that is frequently proposed is to supplement implicit or weak attestations with more explicit, annotated attestations. Instead of using a single number which "scores" the subject, multiple scores might be calculated along any number of axes. For example, instead of "I follow this person", you might want to indicate "I trust this person to recommend movies."

This approach can work in certain contexts like reviews for products or services. But in most cases, getting users to publish such explicit attestations is difficult to incentivize. A good example of this is PGP which, despite the enthusiasm nerds have for building trust graphs, has failed to be widely adopted by non-technical users. The reason for this is that the creation of these attestations has no immediate utility — they are entirely instrumental, requiring up-front investment in order to achieve their purpose. In contrast, follows, likes, and replies all have their own immediate, intuitive incentive.

For this reason, webs of trust will always be more or less implicit, and rely on careful and qualified data analysis. Just because someone is good at recommending recipies does not mean you should trust their political opinions. This is especially true when differentiating between different trust contexts. Trust derived from follow graphs may be very useful for identifying spam or impersonation, but might not be useful for assessing whether someone is safe to meet in a dark alley.

Digital representation of social trust is inherently weaker than authentic social trust, because it is predicated only on the subset of information that can be collected. Major factors in assessing trust in real life (such as physical appearance, credit score, or criminal record) might be entirely absent in a digital setting. This is especially true for new users who don't yet have any attestations from other users about the authenticity or value of their activity.

However, there are additional affordances that Nostr provides which can supplement the trust graph. Synthetic attestations can be generated on behalf of new users by services with an established reputation by reviewing government-issued identification (or by asking for a picture of the person with a shoe on their head). Another method is "proof-of-work", originally invented to frustrate email spam. [NIP 13](https://github.com/nostr-protocol/nips/blob/master/13.md) specifies how a given event can demonstrate that a certain amount of computational work went into its creation. Both of these methods have their limitations (identity theft, AI-generated imagery, and GPU farms can all bypass these measures if the incentive is valuable enough), but they can factor into a more robust trust profile.

## Holding Keys

Cryptographic identity promises a lot, but all of its benefits are predicated on users being able to securely and conveniently hold their private key, which is a big assumption. Over a decade of research has gone into building key storage solutions for Bitcoin wallets. Many of the the complexities and trade-offs involved in those design decisions apply to Nostr as well.

The stakes are slightly different though. If you lose your Bitcoin keys you can lose real money; if you lose your Nostr keys you can lose your social identity. Which one is worse depends entirely on who you are, but both have the potential to be catastrophic.

Nostr also has some disadvantages in comparison with Bitcoin. With Bitcoin you can rotate keys by simply sending funds to a new address and throwing away the old address (although if you lose your key entirely you're still out of luck). On Nostr, your identity is your public key, and therefore much harder to move away from. While nothing prevents copying and re-signing all your social media data with your new key, all references to your cryptographic identity would be broken — and along with them your entire reputation.

Key rotation is something that we have to figure out if Nostr is going to succeed in the long term. There have been some proposals, but none of them have gained enough traction to be implemented. Key rotation is an inherently difficult problem, because you need to borrow the reputation of the old key in order to validate the new key in such a way that an attacker wouldn't be able to do the same thing. Decentralized identifiers (DIDs) are not really a solution because they result either in a circular system of keys or dependence upon a trusted name registrar. Hierarchical keys have the same problem; the root key still has to be competently secured.

There are some things we can do though to make key storage safer and more convenient.

A number of different signer protocols exist as alternatives to pasting your private key into every Nostr client you try, including [browser extensions](https://github.com/nostr-protocol/nips/blob/master/07.md), [Android intent-based signers](https://github.com/nostr-protocol/nips/blob/master/55.md), and [remote "bunker" signers](https://github.com/nostr-protocol/nips/blob/master/46.md).

The last of these is, in my opinion, the most promising. Remote signers can run on any device connected to the internet, and used in any type of application. Browser extension or Android signers can be useful as progressive enhancement, but should always be considered secondary to remote signers.

The difficulty with any of these solutions is that they require new users to learn about and set up an additional component when getting started with Nostr, which is an awful UX from an onboarding perspective. One possible solution to this is for every client to include a remote signer implementation so that users can log into other clients remotely. But this is a lot of complexity to impose on client implementations, and is very difficult to execute successfully.

The most promising solution to the onboarding problem is "multisig" bunkers, which allow for multiple unrelated custodians to coordinate when signing events by breaking the user's private key up into "shards". A scheme like "2 of 3" would require that two custodians collude in order to act on behalf of the user.

But even better in the context of onboarding would be to use a "2 of 2" signature scheme, where half of the key is held by a custodian, and half of the key is held by the client onboarding the new user. This means that unless the client and the custodian collude, the user's key remains under their control. Given the likelihood of non-technical users failing to secure their keys, this can be a viable alternative to self custody for certain people.

This approach can be improved further by sending an email to the new user with a version of their private key [encrypted with a password](https://github.com/nostr-protocol/nips/blob/master/49.md) as a backup. This helps defer the learning process for key management until the user has developed a reputation on the network, making the key valuable. When they're ready to take custody of their key, they'll have it sitting in their email inbox.

One other common pattern worth mentioning is seed words. Seed words are great for securing Bitcoin in cold storage because cold storage ideally requires manual entry onto a physical medium or air-gapped device. A 64-character hex key is going to be a lot harder to write down correctly than 12 or 24 words, especially if you're engraving the characters on steel.

But on Nostr keys are almost always stored on an internet-connected signing device, making them vulnerable in ways bitcoin keys aren't. Seed words only useful for physically backing up Nostr keys that exist only as distributed shards. This can make sense for advanced or paranoid users, but is not really relevant to onboarding new users. In most cases, putting your key in a password manager (optionally encrypted) is enough.