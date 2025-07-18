In 2020, Twitter surprised everyone by censoring several high-profile accounts. This directly contradicted the ethos they had carefully cultivated over the previous decade of being a place where news breaks and ideas can be discussed. When they started censoring political content to appease advertisers, they undermined this journalistic ethos in the same way that mainstream media has been for a long time.

At Twitter's edges, there were some built-in access controls—for example, private accounts and blocking—but the main use case of the platform was to democratize the spread of information and ideas through publicly broadcasted data. Nostr's architecture is well-adapted to this use case, in that it optimizes for censorship resistance and easy distribution of content.

Access controls are similar in many ways to censorship, in that they limit the availability of published data to certain authorized readers. For this reason, an architecture optimized for censorship resistance is necessarily not optimized for access controls or privacy.

I've covered the implications to user privacy of an open network elsewhere, but in this chapter I want to talk about access controls on Nostr from the perspective of digital communities. Communities have a different goal than broadcast social networks, which presents the problem of how (or whether) to adapt nostr to use cases that require access controls.

# Communities are for People

Journalism is about information, facts, and opinions which can be objectified, analyzed, shared and remixed freely. Communities, on the other hand, are about people, whose identities are complex and dynamic, who have a personal experience of the world, are self-interested and responsible for their actions, are self-aware and self-reflective, who have beliefs, intentions, preferences, memory, and imagination.

While the design of any artifact or system requires care to ensure that the designer's intention is solved with a minimum of negative externalities, extreme care must be applied if humans are involved - not only because human life and wellbeing is precious, but also because humans have a unique gift for screwing things up.

The word "community" comes from the latin word "communitatem", which is a contraction of "com", which means "together", and "unitas", which means "unity". So, "community" is "being one, together". This may sound redundant, but it captures the inherent tension of existing in community - the individual is not erased by the community, but is instead uniquely fulfilled in it.

While broadcast social media is monolithic and more or less global, communities are necessarily local and have a distinctive subculture dependent on their membership or stated purpose. Communities, furthermore, are not organized in a single way. Communities may form around a topic, around a cause, around a location, or around a system of values. They may have leadership, or be entirely organic. They may be strict about what kinds of activity is in scope, or they may be much more all-encompassing.

Communities also have a wide range in size. A community could be as small as two people - a single relationship - or it could be as large as millions of people. These two types of communities have almost nothing in common except that they have some definition for who is part of the community.

These three aspects of community - who is included, what kinds of activity are involved, and how many people are participating - form a helpful framework for thinking about community, while an additional fourth dimension concerns how a community is organized.

Organization is downstream of the particular character or purpose of a given community, but is an essential part of maintaining its identity. In this category are the political and technological tools used for maintaining access control, enforcing codes of conduct, and partitioning membership or content into sub-groups.

Unfortunately, understanding the different types of communities (and how to serve them with software) is irreducibly complex, not just because each one is a unique combination of each of these axes, but because people are involved. Communities inherit all the complexity and dynamism of their members.

Communities also exist in community with one another - to the extent that their members interact (or have membership in multiple communities), communities will be affected by each other. A community is therefore itself a higher-level organism which itself inhabits an ecosystem comprised of a whole complex of technologies, contexts, and individuals.

# Digital Architecture

The key thing to keep in mind when designing digital spaces for communities to inhabit is that the responsibility for healthy community functioning is ultimately up to the members and leaders in a given community, but design may be employed to support that functioning.

Designing digital spaces has a lot in common with architectural design, in that the role of the designer is always to facilitate human activity by responding to it, not to impose their own ideas about how a community should function in the abstract.

Also important to keep in mind that any digital space must necessarily have certain concrete characteristics. I think technologists can often fall into the trap of thinking that just because software is infinitely malleable, so are humans. To the extent that a community has certain characteristics, software must be opinionated in supporting those. Conversely, a single digital space will not be appropriate for every community.

Interoperability can improve the situation by allowing different implementations to diverge in design, complexity, branding, and other superficial areas, but some design decisions have to be baked into the protocol layer, particularly in the areas of access and moderation. And just as there are multiple types of buildings for different purposes (factories look quite different from beachfront cabins), there will be different digital spaces which serve different types of communities, which means the protocol layer will have to be adapted to each.

Borrowing from the [New Urbanist](https://en.wikipedia.org/wiki/New_Urbanism) movement, there are a few core elements that every neighborhood should have:

- Spaces should fit the human body, making environments walkable and fostering interaction
- A discernable center, from which the rest of the neighborhood is easily accessible
- A variety of dwelling types, adapted to different demographics
- Shops at the edge of the neighborhood sufficient to satisfy weekly needs
- Streets are narrow, and buildings are close to the street, creating a humane outdoor space
- Prominent sites are reserved for civic buildings

In all of these principles, the goal is to accommodate the needs of the neighborhood's inhabitants - physically, psychologically, and socially. Isolation should be difficult, and access universal.

The application of these principles to digital spaces implies a form of what I like to call "digital localism", which not only mirrors the human scale of real-world architecture and city planning, but is also anchored in it. To that end, here is a short list of principles for digital spaces:

- Digital spaces should fit the human social scale; global broadcast media over-exposes the user, resulting either in loss of privacy, or self-censorship
- Digital spaces should have a discernable center, from which the rest of the space is easily accessible
- There should be a variety of content types, adapted to different use cases
- Utilities like settings, wallets, and administration should be integrated at the edges, not centrally
- Volume of information should be limited (both in terms of how many subdivisions there are, and how much content is in each) in order to avoid overwhelming the user
- Prominent sites are reserved for high-value content. Casual conversations should be more or less ephemeral or private

These principles are intended as a thought experiment, and are by no means normative, but are hopefully helpful for thinking about designing humane digital spaces.

How each of these principles is applied to a given community space will vary based on what type of community is going to inhabit it. Below, I'll list a few different types of community, and how
Below I will propose a few categories of community, and some ideas about how to accommodate each.

- Social clusters
- Small group chats
- Topical discussion forums
- Activity-oriented groups
- Identity-oriented groups

# Social Clusters

In their most organic form, communities exist only as emergent properties of individual relationships within an open network. Another term for this is "social clusters", which can be identified mathematically through graph analysis, or simply by gestalt.

These kinds of communities are open and informally delineated because they are the result of the free association of individuals. And yet they are real and do exist - for example, it's fairly straightforward to assess whether someone is a member of the libertarian community, a particular friend group, or the Christian Church.

None of these communities enforces who can be a member. Political parties and churches might, but individuals are free to associate with anyone willing to associate with them, and each of these examples transcends the particular instances of community within them. This complex of one-to-one relationships and transitive relationships is what forms large open social cluster-based communities, and frequently form the basis for the emergence of more formally-defined communities.
In this type of community, topics of discussion (such as current events) may predicate an actual discussion between individuals, but doesn't usually define a given social cluster on its own.

Social clusters constantly re-form as discussions evolve and relationships form. Clusters also aren't really limited by the Dunbar number, since clustering is transitive, and can grow to billions of members. Member privacy is either protected by virtue of the privacy of individual conversations that feed back into the shared culture of the cluster, or is voluntarily given up in order to attract more attention.

The prominence of various members within a social cluster varies widely as well. Prominent members serve to solidify the group identity by embodying the group's identity as a concrete persona, while the vast majority of members simply follow and either support or register dissent with their "thought leaders", sometimes achieving notoriety themselves, or shifting to an adjacent social cluster. And of course, members may inhabit many social clusters simultaneously, even ones that may not seem adjacent from an analysis standpoint.

This use case is served well by broadcast social media, but is simultaneously supported by smaller-scale forms of association which allow members to evolve the group identity without attracting undesired attention.

# Group Chats

At the other end of the spectrum are group chats. Group chats are a fairly well-defined type of community because in general their members are also well-defined. Many group chats are comprised of only two people, for example text message conversations or direct messages, but can scale to dozens, or even hundreds, of members.

Group chats are defined by there being a relationship between each member. It may be that multiple people are added to a group chat who don't have a pre-existing relationship, but because every member is necessarily a recipient of every message, every member is implicitly connected.

Stated more formally, if there are `n` members in a group, there are `n * (n - 1) / 2` connections between members. The number of relationships, and therefore the complexity of the social dynamic, increases quadratically as the number of members increases.

This is of course also true of regular in-person social dynamics. When one person is added to a conversation, the dynamic completely changes. If another person then leaves the conversation, the dynamic changes again. A palpable change in tone and topic occurs depending on the conversation's members.

Because of the each member pair necessarily has a unique relationship, the requirement that there be a high level of trust (or willingness to engage with other members) within the group is more strict than in any other type of community. Every conversation involves all members, meaning sidebar conversations are impossible without creating a separate group with a subset of members. This becomes more awkward as the group grows.

To complicate matters, trust is not binary or even one-dimensional. You don't either trust someone or not trust them, you trust them to a greater or lesser extent. Furthermore, you may trust someone in certain areas, but not in others. I might trust a friend to recommend a book, but not to watch my children.

In a conversation with only one other person, what information you share depends exclusively on your relationship with that person. But the moment you introduce someone else to the conversation, what information can be shared is limited by the _least_ trustworthy member of the group.






Because trust may be many-dimensional, you may be willing to talk about one topic with Alice, and topic B with Bob, but not B with Alice or A with Bob, leaving you very little to say.

The result of this is that as the size of a group grows, chats often go through a process of growth and subsequent stagnation. You invite your five close friends, they invite their friends, and before you know it, the group has 50 members, and no one's willing to say anything because they don't know everyone in the group. And so the default trust profile within a group between members who don't know each other is complete distrust.

For this reason, the medium of group chats simply cannot scale. What is required to make small groups scale is partitioning, which I will get to in a later section. But just for illustration, if within a chat you could create a sidebar conversation, you would be creating an entirely separate chat group, but in the context of the original, allowing you to have a conversation that is accessible to the rest of the group, but isn't broadcasted to all of them.

For this reason, chat groups tend to be either ephemeral and practical, organized around some short-term need for coordination, or they are predicated on a high level of relational trust shared between all members of the group.

# Discussion Forums

Now let's bounce back again to the other end of the spectrum. Just this side of social cluster type communities are discussion forums.

Discussion forums are not formless and self-assembling like social clusters are, and neither do they require high levels of trust like small groups. Instead, discussion forums are predicated upon some raison d'être—a topic of conversation. This topic can range from auto repair of a particular vehicle to Monty Python fandom to discussions of history.

In every case, the thing that is the primary draw for members into the community is some object or idea. Discussion forums may be educational, they may be oriented at entertainment, at professional development, or even as a place for people to connect over emotional trauma or shared illness.

Discussion forums are not at odds with people, but they are abstracted from them. It would be inappropriate to start a political polemic on a discussion forum centered around gluten intolerance. It's not that your political opinions are invalid as an individual to hold, it's that you are in a particular room that has been cleared for conversation about a particular thing.

At the same time, many discussion forums have a general room or a random room or an off-topic room where things unrelated to the topic at hand can be discussed. This is a recognition that when people come together and form relationships and community around topics, they may not know each other to begin with. The only cornerstone of their relationship might be the desire to identify edible mushrooms, but over the course of those conversations, other aspects of their identity are revealed. This can lead to business relationships, friendships, or even marriages.

Discussion forums are not in themselves dysfunctional, but exclusive interaction with discussion forums is. Discussion forums, on their own, cannot satisfy all parts of a person's identity, even for a person who is exceptionally one-sided. So there may be a complementary part of that person's social experience offline.

Meetups are the real-life analog to this. You might need to go jogging with other people or learn the game of go. These activities are the starting point for the emergence of new relationships of different types and which seek their fulfillment in a different type of venue.

Discussion groups are almost like an artificially delineated version of social clusters, in that their membership is completely informal and discussion forums' membership is almost entirely open except to spammers or people who don't follow the discussion forums' guidelines—for example, by flaming, going off topic, et cetera.

This poses a dilemma. Discussion forums are essentially open in that the conversation surrounding a given topic should not be gatekept by any particular person.

If, for political reasons or personal reasons, certain people with a legitimate interest in a discussion topic are kept out of that space, that constitutes an abridgment of their freedom of speech. Not under the law, but in a social sense. Because the administrators of the discussion forum have substituted their role as guardians of the conversation for their own personal interests and biases. Sometimes this is necessary because a lot of the time people just can't be in the same room together and still be civil, which is unfortunate, but also a reality.

This results in the dynamic that is seen frequently on Reddit and Mastodon, where moderators get to run the discussion forum as their own private fiefdom and ban other members at will.

Frequently the solution to this is to fork the discussion forum and create duplicate versions of the same topic. But this breaks down network effects. An example of this is Reddit has left-wing meth users and right-wing meth users forums, because the meth users can't keep their politics out of talking about meth. But this of course breaks down network effects, which is part of the core value proposition of having a discussion forum in the first place—people with different backgrounds can have different perspectives on the same topic, and this can be valuable.

The reason this ends up happening is because discussion forums are centralized. And this is the place that Nostr can step in to improve the status quo. Because discussion forums involve centralized administration, they necessarily fragment, because the topic, which is owned by no one, is coupled with the infrastructure, which is owned by someone.

Nostr's multi-master architecture can help solve this. If a member of a discussion forum chooses to fork the group to their own relay with different moderation policies, they can do that and the two groups are still interoperable, and a user who is a member of both can relate the two and merge the content.

This is essentially how NIP-29 works, where a group belongs to a relay. The same group—but the group ID is just a string—and so the same group can be running on a separate relay. And if you're a member of the group on both relays, you get the superset of content across the two versions.

Other versions of this could be imagined that are not supported by relay administration in particular, but where moderation is a function of user preferences. Users might choose to see all posts, regardless of moderation, or only posts that have been approved by moderators, or select their own moderators, or use web of trust or proof of work heuristics to filter posts.

All of these are legitimate options in a discussion forum context because missing data is not essential to the conversation. Because the members involved in the conversation are frequently numerous, the conversation is very broad. And the ability for a user to filter down to the parts of the conversation that they're interested in is the user's prerogative.

In this sense, missing data isn't a bug. And there isn't FOMO because the user has chosen policies that cause that data to be missing. This is one of the neat things about Nostr: it is partition tolerant. And that's part of the point. Not everyone needs access to everything.

Despite these different strategies for moderation, there's the complexity of building a protocol that properly handles discussion forum type communities.

NIP-72 was an attempt at building this, but unfortunately it was overprescriptive. Not only did it define how moderators are selected, which should be out of scope given that Nostr's purpose is for giving the end user control over their experience, but it also prescribed that posts should not be shown unless moderators approve the posts. Which means in order for a discussion forum to function, you need highly active and invested moderators approving manually every post.

But this is not how discussion forums begin. They start as unmoderated groups, and ownership and administration grow as the group grows to accommodate the problems that are associated with scale.
And to the extent that the leadership of the discussion forum fails to grapple with the difficulties of managing a group on a social level, the group itself will fail. This is, again, not a technical problem. It's a human problem. Even on the level of something as seemingly neutral as a discussion forum.

The discussion forum group type is not limited to forums or subreddits, but can be seen anywhere that open access is granted to participate without any prior relationship being established. For example, livestream chats, discord servers, or blog post comment sections. In any of these cases, the user can simply register, leave their comment, and never come back if they so desire. Access control is only implemented when a participant breaks the rules or expectations of the discussion forum, whether by posting spam, harassing other users, or going off-topic.

# Owned Groups

# Commons

# Roles and Membership

- Membership is not binary

# Scale and Trust

# Subdivisions

- By topic
- By content type
- By identity

# Aligned Storage and Encryption

# Managing Complexity
