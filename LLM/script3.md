# PART THREE – HOW DOES AN LLM UNDERSTAND THE CONTEXT OF A SENTENCE?

Imagine naan unga kitta, "I went to the bank" nu solren.

Inga bank-na enna?

Money deposit panra bank-ah?

Illa river pakkathula irukkura bank-ah?

Indha sentence mattum vechu exact meaning decide panradhu konjam difficult.

Aana naan, "I went to the bank to deposit money" nu sonnaa meaning clear aagidum.

Ippo, "I sat near the bank of the river" nu sonnaa vera meaning.

Same word. Aana surrounding words change aagumbodhu meaning-um change aagudhu.

Human beings idha context use panni understand pannuvom.

Language model-um sentence-la irukkura words-oda relationships-ah calculate pannum.

Indha concept-ah understand panna namakku oru important mechanism venum.

Adhu dhaan attention.

Imagine neenga oru paragraph read panreenga.

Andha paragraph-la oru person's name mention pannirukkaanga.

Next sentence-la "he" nu varudhu.

Andha he yaarai refer pannudhu-nu kandupidikka, previous sentence-ah thirumba paapom.

Adhaavadhu, oru word-ah understand panna, adha suthi irukkura other words-um namakku help pannudhu.

Language model-la indha maadhiri relationships calculate panra mechanism-ku self-attention-nu peru.

Self-attention-na, oru sentence-la irukkura words, adhe sentence-la irukkura other words-oda evlo relevant-ah irukku-nu calculate panradhu.

Ippo idhu epdi calculate aagudhu-nu paakalaam.

Attention mechanism-la three important things irukku.

Query, Key and Value.

Idha library example-la understand pannalaam.

Neenga library-ku poi oru particular topic pathi book thedureenga-nu imagine pannunga.

First, neenga enna thedureengalo adhu unga Query.

Library-la available-aana books-oda identifying information Keys maadhiri.

Andha books-kulla irukkura actual content Values maadhiri.

Computer-la idhellam numbers and mathematical operations moolama nadakkum.

Model ovvoru token-ukkum Query, Key and Value representations create pannum.

Query and Key compare panni, endha token evlo relevant-nu calculate pannum.

Andha relevance use panni Value information combine pannum.

Ippadi surrounding words-oda information current word representation-kulla influence pannum.

Idhukku oru mathematical formula irukku.

Screen-la formula paakumbodhu bayapada vendam.

Namma already concept-ah understand pannitom. Ippo formula-la adhu eppadi represent aagudhu-nu paapom.

Attention of Q, K and V equals softmax of Q multiplied by K transpose, divided by square root of D K, and then multiplied by V.

Inga Q-na Query.

K-na Key.

V-na Value.

First Query and Key compare panrom.

Next, relevance scores calculate panrom.

Softmax-nu oru mathematical operation use panni, indha scores-ah weights-ah convert panrom.

Weight-na evlo importance kudukkanum-nu represent panra value.

Finally, andha weights use panni Value information combine panrom.

So, idhu dhaan attention calculation-oda basic idea.

Ippo varaikkum namma enna paathom?

Oru sentence-la irukkura words-ah model numerical representations-ah convert pannudhu. Attention mechanism use panni, oru word-ku surrounding words evlo relevant-ah irukku-nu calculate pannudhu. Andha relevance base panni information combine pannudhu.

Aana inga oru interesting question varum.

Oru sentence-la different types of relationships irukkalaam la?

For example, oru word-oda grammatical relationship, innoru word-oda meaning relationship, vera oru word-oda context relationship-nu different patterns irukkalaam.

Appo model ore attention mechanism-ah mattum use pannuma?

Illa. Adhukkudhaan multi-head attention use pannuvanga.

Imagine neenga oru movie review padikkureenga.

Oru angle-la story nalla irukka-nu paakreenga. Innoru angle-la acting epdi irukku-nu paakreenga. Vera oru angle-la music and visuals epdi irukku-nu paakreenga.

Same movie dhaan. Aana different perspectives-la evaluate panreenga.

Multi-head attention-um different attention heads moolama information-ah different learned perspectives-la process pannum.

Each head-kum separate learned projections irukkum.

Aana inga oru important point. Oru particular head kandippa grammar mattum dhaan understand pannum, innoru head meaning mattum dhaan understand pannum-nu fixed-ah solla mudiyadhu. Training moolama different patterns learn aagalaam.

Ippo attention mudinja udane model answer kuduthiduma?

Illa.

Attention-ku apram feed-forward network irukkum.

Feed-forward network-na, already collect panna information-ah additional neural network layers use panni process panradhu.

Simple-ah sollanumna, attention surrounding words-lendhu useful information collect panna help pannudhu. Feed-forward network andha information-ah further transform panna help pannudhu.

Next, residual connection.

Idha simple-ah understand pannalaam.

Neenga oru long calculation panreenga-nu imagine pannunga. Oru stage-la irundhu next stage-ku pogumbodhu, earlier information-ah completely lose pannida koodadhu.

Adhukku shortcut maadhiri oru connection irundhaa useful-ah irukkum.

Residual connection-um information flow-ku indha maadhiri shortcut provide pannum.

Adhukku apram layer normalization.

Layer normalization-na, neural network-la values-oda scale and distribution stable-ah maintain panna help panra technique.

Idhu training and processing stable-ah irukka support pannum.

So, namma ippo paatha components ellam serndhu oru Transformer block create aagudhu.

Attention, feed-forward network, residual connections and layer normalization.

Indha components oru structured sequence-la work pannum.

Ippadi pala Transformer blocks one after another stack pannappadum.

Idhudhaan Transformer architecture-oda important foundation.

Ippo GPT maadhiri text-generation models pathi konjam paakalaam.

GPT models-la decoder-only Transformer architecture use pannuvanga.

Inga oru important mechanism irukku. Adhu causal masking.

Causal masking-na, oru position-la irukkura token, future-la varra tokens-ah paakka mudiyadhu.

For example, "The sun rises in the east" nu oru sentence irukku-nu imagine pannunga.

Model first token process pannumbodhu, future-la varra words-oda information-ah use panna koodadhu.

Yenna, model next token predict panna dhaan learn pannudhu.

So, current position-ku available-aana previous information mattum use panna allow pannuvanga.

Idhukkudhaan causal masking use aagudhu.

Ippo namma indha section-la enna learn pannom?

Token representations-la irundhu attention varaikkum, attention-lendhu Transformer blocks varaikkum, andha blocks-la irukkura different components varaikkum paathom.

Ippo vectors, matrices and dot products pathi innum detailed-ah understand pannanum-na, namma website-la irukkura Machine Learning course-ah kandippa check pannunga.

Andha course-la Module Three and Module Eight-la indha concepts-oda clear explanations and detailed topics irukku.

So, indha LLM course-ah complete pannadhukku apram, andha modules-ah visit panni paathaa, inga namma discuss panna concepts innum clear-ah puriyum.

Aana oru important question innum answer aagala.

Indha model-ku language patterns epdi learn aagudhu?

Adhu dhaan namma next section.
