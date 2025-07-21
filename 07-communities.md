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

In a conversation with only one other person, what information you share depends exclusively on your relationship with that person. But the moment you introduce someone else to the conversation, what information can be shared is limited by the _least_ trustworthy member of the group. And because trust is multi-dimensional, you may be willing to talk about topic A Alice, and topic B with Bob, but not B with Alice or A with Bob, leaving you very little to say.

The result of this is that as the size of a group grows, chats often stagnate. You invite your five close friends, they invite their friends, and before you know it, the group has 50 members, and no one's willing to say anything because they don't want to bother everyone in the group.

For this reason, the medium of group chats simply cannot scale without a way to limit the scope of a given conversation to a subset of the group. In practice, this feature is not usually included in group chat implementations - instead, users are encouraged to create an entirely different group.

For this reason, chat groups tend to be either ephemeral and practical, organized around some short-term need for coordination, or they are predicated on a high level of relational trust shared between all members of the group.

# Discussion Forums

Let's bounce back now to the other end of the spectrum. Just this side of "social cluster" type communities are "discussion forums".

Discussion forums are not formless and self-assembling like social clusters are, and neither do they require high levels of trust like small groups do. Instead, discussion forums are predicated upon some raison d'être -  in other words, a topic of conversation. This topic can range from auto repair to Monty Python fandom to mathematics.

In every case, the thing that draws members into a community is some object or idea of common interest. Discussion forums may be educational, oriented toward entertainment or professional development, or even places for people to connect over emotional trauma or shared illness.

Discussion forums are not at odds with people, but they are abstracted from them. It would be inappropriate to start a political polemic on a discussion forum centered around gluten intolerance. Doing so would be equivalent to going to your local health food co-op and canvassing for a particular political candidate.

At the same time, many discussion forums have an "off-topic" room where things unrelated to the topic at hand can be discussed. This is a recognition that when people come together and form a community around a particular topic, they may form relationships that transcend their original context.

Meetups are a real-life analog to discussion forums. You might want to go jogging with other people or learn the game of Go. These activities are valuable in themselves, but can also serve as a starting point for building social relationships that are best served by a different venue.

Discussion groups are similar to social cluster-type communities, in that their membership is largely informal and open (except to people who don't follow the norms of the community). This poses a dilemma. Discussion forums are essentially open in that the conversation surrounding a given topic should not be gatekept, but at the same time moderation is required to keep discussion "on topic".

This results in a dynamic frequently seen on Reddit and Mastodon, where moderators end up treating a discussion forum as their own private fiefdom, enforcing rules arbitrarily, and banning other members at will.

Discussion forums frequently fragment when they reach a certain size because the topic, which is owned by no one, is coupled with group infrastructure, which is owned by someone. But this breaks down the forum's network effect, which is part of the core value proposition of creating a digital space in the first place - to gather people interested in a topic in _one_ place.

Nostr's multi-master architecture can help solve this. If a member of a discussion forum chooses to fork the group to their own relay with different moderation policies, they can do that without sacrificing interoperability. A user who is a member of both can participate in both at once, merging the content in one interface.

This is essentially how NIP-29 works, where a group "belongs" to a relay, but multiple versions of the same group can exist simultaneously. If you're a member of the group on both relays, you get the superset of content across the two versions.

Other versions of this could be imagined that are not necessarily supported by relays, but where moderation is a function of user preferences. Users might choose to see all posts, regardless of moderation, or only posts that have been approved by moderators, or select their own moderators, or use web of trust or proof of work heuristics to filter posts.

All of these are legitimate options in a discussion forum context because missing data is not essential to the conversation. Because there are frequently a large number of  members involved in the conversation, the conversation is very broad. Filtering the conversation based on the relationship a user might have to various social clusters within the discussion forum is the user's prerogative.

In this sense, missing data isn't a bug. FOMO isn't a problem because the user himeself has chosen policies that cause that data to be missing. This is one of the neat things about Nostr: it is partition tolerant. Not everyone needs access to everything.

In practice, Nostr implementations of discussion forums haven't gotten this right. NIP-72 was intended to be "reddit on Nostr", but ended up killing communities by being overprescriptive. Not only did it define how moderators are selected, (which should be out of scope given that Nostr's purpose is for giving the end user control over their experience), but it also prescribed that posts should not be shown unless moderators approve the posts. Which means that in order for a discussion forum to function, you need highly active and invested moderators manually approving every post.

But this is not how discussions grow. They start out informally, and unmoderated, adding moderation as problems accumulate as a result of scale.  To the extent that the leadership of the discussion forum fails to grapple with the difficulties of managing a group on a social level, the group itself will fail. This is not a failure of technology, but of the people managing the group.

The discussion forum group type is not limited to forums or subreddits, but can be seen anywhere that open access is granted to participate without any prior relationship being established. For example, livestream chats, discord servers, or blog post comment sections. In any of these cases, the user can simply register, leave their comment, and never come back. Access control is only implemented when a participant breaks the rules or expectations of the discussion forum, whether by posting spam, harassing other users, or going off-topic.

# Owned Communities

Next up we have "owned" communities, which are similar to but distinct from discussion forums. Discussion forums are predicated on some general topic that doesn't necessarily belong to any of the members, whereas owned communities are organized by, and for the sake of, some centralized entity.

One example is Patreon members' areas, which attract users by virtue of their interest in the content creator, who has the right to kick anyone out of "their" space at any time. Internal company chats on (say) Slack, are another example. Access to the chat is justified by a person's status as a member of the company and is revoked when that membership ends.

If the company or content creator decides to move the community to a new platform (or delete it entirely), that's their prerogative. Members have neither the right nor the incentive to move discussion to a platform not owned by the topic of discussion, because the whole point is to be close to that person or entity. Doing so would make the group into a discussion forum, because it would then be a group of outsiders, rather than a group of "members".

This kind of community is inherently centralized, and so centralized control is a feature, not a bug. The system administrator and the owner of the community are either the same person or have a relationship of some kind. The admin may be an individual contractor, but more often than not it's a software platform.

Companies rent Slack (the product) from Slack (the company) because they don't want to bring the administration of a chat solution in-house. This is a reasonable decision, but comes with certain costs—namely the platform users' privacy and security.

To the extent that an entity is likely to be deplatformed by the third party they've contracted to host their chat platform, they should consider an alternative third party or a self-hosted solution. Hosting platforms also frequently harvest user data, either for the purpose of showing ads or (if the platform is a paid solution) for the purpose of analysis. This analysis can be responsible, or it can be parasitic. There's an inherent conflict of interest here, even leaving aside the possibility of governments asking platforms for user data.

Because of the characteristics of owned communities, they don't benefit from a protocol optimized for decentralization per se. Although to the extent that they interoperate with other products using the same protocol, they may be able to provide a superior value proposition in the form of cryptographic identity support, signed data, and protocol-native content types.

# Commons

Finally, we have a type of community which I'm calling a "commons". This may not be the best name for it, but the idea is that this type of community is "owned" in common by its members. These groups may form for any of the reasons that characterize the other community types I've mentioned, but in contrast to "owned" communities implement self-organization through political means.

What I mean by "politics" is not mere bureaucracy, but the creation of an environment that a community inhabits, through the activity of its members. Fisher Ames described it this way:

> Politicks is the science of good sense, applied to public affairs, and, as those are forever changing, what is wisdom to-day would be folly and perhaps, ruin to-morrow. Politicks is not a science so properly as a business. It cannot have fixed principles, from which a wise man would never swerve, unless the inconstancy of men's view of interest and the capriciousness of the tempers could be fixed.

Politics involves values, responsibility, individual agency, leadership, and compromise. In other words, it is a social phenomena which seeks to resist the entropy of conflict by structuring reality into something hospitable to its inhabitants. In this way, a digital commons must be organized in the same way as a state, a city, or a home.

Self-organization does not imply a particular mode of organization, like a democratic voting system or a cryptographic DAO. While a decentralized system of voting or staking might be interesting (and appropriate to certain communities), more conventional centralized techniques can still be used to manage a commons-type community insofar as they don't conflict with the community's ability to self-organize politically.

But in a commons-type community, the roles that a given member takes on are especially important, because the commons is sustained by its members willingness to take participate in its cultivation. A commons-type group is not only an environment in which a community exists, but the product of its members' activity.

Whatever the organizing principle chosen by the community, the digital spaces it inhabits should accommodate it rather than impose its own structure upon it. As a result, commons type communities are a very large, and very difficult, design space. They can be supported by chat applications or by owned group models, or even by digital spaces originally intended for discussion groups or broadcast social media. But the selection or construction of a digital space must be carried out in close partnership with the actual members of the community.

# Roles and Spaces

In the vast majority of communities (not just commons-type communities), membership is not binary, but exists on a spectrum. This is obvious in terms of moderation and administration. If not all members are moderators, some members have a role which grants them privileges not accorded to the other members of the group.

But membership has other kinds of gradation in both formal and practical terms. Formally, members may be granted access only to certain parts of the group or certain abilities. Their content may be promoted more or less to other members of the group.

Alternatively, members may be afforded the same nominal status as other members, but participate more or less frequently. Their influence within the group may increase or decrease organically based on the esteem that their peers have for them, and not based on any procedural mechanism.

An example of gradations of membership in the real world is that of catechumens, which in the Eastern Orthodox Church are not permitted to partake in the Eucharist until they are baptized and chrismated. In the past, catechumens were even excluded from the second half of the liturgy. This represents a literal architectural partition which distinguishes between members.

These distinctions are nearly universal. The vast majority of communities benefit from some form of partitioning of the spaces they inhabit. In a digital space, these partitions can be erected along three different axes: identity, topic, and content type.

Splitting a space up by identity means applying a different set of access controls to different members of the group. For example, within a chat application you might have locked rooms that are accessible only to certain members. Access is granted based on the member's role, either in a social sense or in a formal sense - for example, depending on whether they've paid a subscription in order to gain access.

Partitions based on identity may not necessarily be enforced with access control, but might exist for other reasons. Conversations may simply be irrelevant to certain members of the community, rather than necessarily private.

Digital spaces may be partitioned along topical lines as well. These may be longer - lived topical discussions — for example, a "general" topic or an "announcements" room — or they may be shorter-lived topical divisions - for example, a conversation related to planning an upcoming event.

Topical divisions exist for user convenience and to allow users to opt out of messages they're not interested in. This allows the community as a whole to function without cluttering the common area.

Finally, digital spaces may be partitioned by content type. For example, you might have a company calendar which is accessible to all members, and which includes events of any topic or author, but which only includes events - not microblogging posts or chat messages.

Calendars are an obvious version of this, but partitioning by content type can be used to good effect in other ways as well. Certain conversations are better served by rapid-fire short chat messages, which are often use more synchronously than other forms of written media. Other discussions might best be served by long, thoughtful posts embedded in a slower medium, like a series of articles. Some content may also be more or less ephemeral, depending on content type. For example, a wiki should last pretty much as long as the community does, whereas chat messages can be allowed to recede into memory and potentially even be deleted after some time.

All three of these partitioning schemes - by membership, topic, or content type - can be combined. For example, maybe only the company secretary can create events on the company calendar. Or maybe only the church pastor can start a live stream. Similarly, certain members might have access only to certain topics.

And as usual, wherever there are interactions between different things, you get combinatorial complexity. Special cases can be nuanced literally forever. A software developer's job is never done because software is essentially the management of emergent organic social complexity with linear, propositional, systematic tools.

Maybe AI will change all of this. Introducing AI agents into a community context can be a great way to empower members to use the community's infrastructure in unexpected ways, whether to do search and analysis, create new software solutions, or simply accomplish one-off tasks. The deep integration of AI into software solutions in general, and communities in particular, is inevitable, but care should be taken to anticipate negative externalities that might result from its use.

If, for example, a community includes an AI search tool in order to ask the community as a whole a question, this can actually result in the slow dissolution of the social bonds that hold a given community together. In other words, even if the question "where can I find raw milk locally?" is answered ad nauseam, the question itself serves as a basis for the development of relationships. The best way to get to know your neighbors is to ask them for a favor.

This social engagement creates real interdependence and mutual understanding and is easily displaced by software solutions like knowledge bases, AI agents, and frequently asked questions. These tools aren't without utility, but are easily misused. The discipline of design is essential to the task of designing community spaces.

# Managing Complexity

In every community scenario, there is significant complexity involved in implementation. Different group protocols on Nostr have attempted to manage this complexity in different ways.

Some, like NIP 72, NIP 48, and Nostr MLS manage complexity in the protocol itself. Others, like NIP-29, offload much of the complexity to the implementation by means of server scripting or other customization.

This has an important trade-off in terms of flexibility and applicability to a given community. The more functionality is defined by the protocol, the less able a given community is going to be to adapt the protocol to its own purposes.

This relates to the decision on whether to use encryption or server-side access controls to enforce access control policies.

In an encryption-based digital space implementation, all clients have to be on the same page about what the group policy is, which means administration and consensus has to be baked into the protocol itself. This may be done using a plugin architecture, like what MLS has, but all clients still have to enforce the same set of rules.

In general, lifting complexity into client implementations is the right decision because relays are dumb repositories. But this is only true with respect to content type support, not necessarily with respect to community organization, which is a form of access control and therefore belongs to the domain of relays.

By pushing the implementation complexity of access control and membership policies down to the relay, it becomes much easier to build interoperable clients. Because all the client has to do is speak the content-type part of the protocol, the relay can be allowed to manage access control and content curation using any method without increasing the surface area of the interface that it exposes.

Trusted servers can also implement any policy encrypted groups can, including forward secrecy and post compromise security (albeit in a "simulated" way). Whether to use servers to enforce group policy rather than a protocol leveraging encryption becomes a question of whether the group's need for security and privacy outweigh its need for a highly-customized implementation. Server-enforced policies are going to be much cheaper to implement too, since no protocol work has to be done.

At the same time, almost anything a server can be automated within the scope of an encrypted group. For example, if group access is granted or revoked based on the status of a member's subscription (in the case of a paid group), a program acting on behalf of a group moderator can implement whatever policy is needed. So while encrypted protocols may be more rigid and require more careful design than server policies, they are almost certainly a more robust solution over the longer term.

# Interface Complexity

Even in the case of server-enforced policy, clients can't be entirely passive. At the very least, the different partitioning schemes I enumerated earlier has to be supported by the interface that clients expose. However, different clients may provide a different interface to the same groups. An interesting question here is whether a diversity of interfaces makes digital spaces more or less habitable.

Imagine that you could cook a meal with someone else in two separate kitchens simultaneously. You could use your kitchen, which you're familiar with, they could use theirs. And if you have an appliance that they lack, they can hand the food over to you, and you can use the appliance to process it.

Different clients have different affordances. In some ways, this is obviously necessary. An administrator is going to need administrative tools, which are going to be completely inert if presented to a regular, unprivileged user.

But what about the partitioning of content? If one user uses a client which lumps all chat conversations into a single view and another one separates them by topic, will this cause failures of communication?

In some cases, I think, yes. The only real solution to this is to include expected behavior in the specification. For example, NIP C7 is one of the smallest NIPs in the Nostr repository, in that it simply defines a kind that's used for chat messages with almost no other concerns. But in that NIP is the stipulation that reply hierarchies must not be deeply nested, but should instead be presented linearly. This provision is completely unenforceable, but is vital for providing the same user experience across clients.

In this chapter I've only scratched the surface of what communities are and how to serve them best within a digital medium. This should be treated only as a starting point for further development of these ideas. And when developing solutions for communities, we should not be afraid of a multiplicity of protocols because different protocols provide a different level of accommodation to different types of community.
