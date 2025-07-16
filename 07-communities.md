Nostr's architecture is well suited to certain problems and less so to others, even though it's applicable to a wide range of applications. In particular, Nostr was created and gained its popularity as an alternative to public broadcast social media platforms like Twitter.

In 2020, Twitter surprised everyone by censoring numerous high-profile accounts. This directly contradicted the ethos they had carefully cultivated over the previous decade of being a place where news breaks and ideas can be discussed. There are numerous slogans Twitter used to signal this value proposition, such as claims that they're the "public square."

When they started censoring, they undermined this journalistic ethos in the same way that mainstream media did.

Nostr's architecture is quite good for filling this use case. Twitter's use case was characterized primarily by publicly broadcasted data, not by permissioned access. At the edges, there were access controls—for example, private accounts and blocking. But the main use case of the platform was to democratize the spread of information and ideas. Nostr works well for this because identities are public. The moment you sign an event, you're publishing your public key along with it. And events, conventionally, are published to multiple relays for the purposes of avoiding censorship.

In a sense, access controls are censorship because they limit the availability of published data to certain readers. And so an architecture optimized for censorship resistance is an architecture that is not optimized for access controls or privacy.

I've mentioned before the implications to user privacy of an open network, but in this chapter I want to talk about access controls on Nostr from the perspective of digital communities. Communities have a different goal than broadcast social networks.

Journalism is about information, facts, and opinions, which can be objectified, analyzed, shared and remixed freely. Communities are about people. Facts and opinions are nouns. People are actors and are complex and multifaceted. Dealing with subjects is far more difficult than dealing with objects.

It might be helpful to define the word "community" here. I always find etymology to be especially revealing - "community" comes from the latin word "communitatem", which is a contraction of "com", which means "together", and "unitas", which means "unity". So "community" is "being one, together". This may sound redundant, but it captures the inherent tension of existing in community - the individual is not erased by the community, but is instead uniquely fulfilled in it.

While broadcast social media is monolithic and global, communities are necessarily local and have a distinctive subculture dependent on their membership or stated purpose. Communities, furthermore, are not organized in a single way. Communities may form around a topic, around a cause, around a location, or around a system of values. They may have leadership, or be entirely organic. They may be strict about what kinds of activity is in scope, or they may be much more all-encompassing.

Communities also have a wide range in size. A community could be as small as two people - a single relationship - or it could be as large as millions of people. These two types of communities have almost nothing in common except that they have some definition for who is part of the community.

These three aspects of community - who is included, what kinds of activity are involved, and how many people are participating - give use a helpful framework for thinking about community. Unfortunately, understanding the different types of communities (and how to serve them with software) is irreducibly complex, since every individual community is a unique combination of each of these axes.

A fourth dimension of community concerns how a community is organized. This is downstream of the particular character or purpose of a given community, but is an essential part of maintaining its identity. In this category are the political and technological tools used for maintaining access control, enforcing codes of conduct, and partitioning membership or content into sub-groups.

# Being and Becoming

# Talking and Doing

# Scale and Trust

# Social Clusters

[This is the beginning of the organization section]

In their most organic form, communities exist only as emergent properties of individual relationships within an open network. Another term for this is social clusters, and they can be identified by graph analysis or just simply gestalt.

These kinds of communities are open and not well defined because they are the result of the free association of individuals with other individuals. And yet they are real and do exist. It's fairly straightforward to assess whether someone is a member of the English-speaking community, or the libertarian community, or the Christian community.

None of these communities enforce who can be a member. English as a second language groups, or political parties or churches might, but individuals are free to associate with anyone willing to associate with them. This complex of one-to-one relationships and transitive relationships is what forms large open social cluster-based communities.

These are not the communities that I'm going to be talking about in this section since they do not rely on a formal definition of membership or on any kind of access control.

The kind of community that I'm focusing on here are gated communities that have administrators or leaders or infrastructure or a distributed mechanism for granting or restricting access to community members or community content.

# Who and What - relationship between identity and activity

# Partitioning Schemes

# Aligned Storage and Encryption

# Managing Complexity
