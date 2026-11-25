PART FIVE – HOW DOES THE MODEL CHOOSE ITS NEXT WORD?

Ippo namma model already train aagiduchu.

Training moolama model language patterns learn panniduchu. Ippo namma adha use panni questions kekkalaam, answers generate panna sollalaam.

For example, neenga ChatGPT-kitta oru question kekkureenga.

Andha model-oda already learned weights use panni answer generate panra process-ku inference-nu peru.

Inga oru important difference irukku.

Training time-la model language patterns learn pannum. Inference time-la already learned information use panni namakku answer generate pannum.

Ippo indha answer epdi generate aagudhunu step by step paakalaam.

Suppose naan model-kitta oru sentence kudukkuren.

"My favourite programming language is..."

Ippo model next enna word varalaam-nu calculate pannum.

Maybe Python, Java, C++ or JavaScript.

Aana model indha words-la edha choose pannum?

Adha understand panna first logits and probabilities pathi konjam paakanum.

Model possible next tokens-ku different numerical scores generate pannum.

Indha raw scores-ku logits-nu peru.

Indha logits-ah probability values-ah convert panna softmax use pannuvanga.

Probability-na oru particular word select aagura possibility-ah numerical value-la represent panradhu.

For example, model output-la Python-ku sixty percent probability, Java-ku twenty-five percent probability, and C++-ku fifteen percent probability irukku-nu imagine pannunga.

Ippo unga kitta oru question.

Python-ku highest probability irukku.

Appo model kandippa Python-ah dhaan select pannuma?

Answer, not always!

Because next token select panna different methods irukku.

First, greedy decoding.

Greedy decoding-na, highest probability irukkura token-ah direct-ah select panradhu.

Namma example-la Python-ku highest probability irukku. So, greedy decoding use panninaa Python dhaan select aagum.

Simple, right?

Aana every time highest probability word-ah mattum select panna, output konjam predictable-ah irukkalaam.

Sometimes different possible words-lendhu select panna vendiyirukkum.

Adhukkudhaan sampling use pannuvanga.

Sampling-na, model calculate panna probability values base panni possible tokens-lendhu oru token select panradhu.

For example, Python-ku sixty percent probability, Java-ku twenty-five percent probability, C++-ku fifteen percent probability irundhaa, Python select aagura chance adhigam.

Aana Java or C++ select aaguradhukkum chance irukku.

So, greedy decoding highest probability token-ah select pannum.

Sampling probability distribution base panni token select pannum.

Ippo sampling-la innum oru interesting setting irukku.

Adhu dhaan temperature.

Temperature – How predictable should the answer be?

Idha understand panna namma oru small activity pannalaam.

Imagine naan unga kitta oru sentence start panren.

"On a rainy day, I would like to..."

Ippo unga mind-la enna words varudhu?

Sleep? Watch a movie? Drink coffee? Read a book?

Different people different answers solluveenga, right?

AI-kum next word select panna multiple possibilities irukkum.

Aana indha possibilities-la model evlo strongly highest probability word-ah prefer pannanum-nu control panra setting dhaan temperature.

Simple-ah sollanumna, temperature controls how concentrated or spread out the probability distribution is.

Ippo rendu situations imagine pannunga.

First, temperature romba low-ah irukku.

Appo highest probability irukkura word-ku more preference kidaikkum.

So, model mostly predictable-ah irukkura option-ah select pannum.

Second, temperature konjam high-ah irukku.

Appo probability distribution spread aagum.

Adhanaala other possible words-ukkum select aagura chance increase aagalaam.

Ippo unga kitta oru quick question!

Temperature low-ah irundhaa output more predictable-ah irukkuma?

Correct!

Temperature high-ah irundhaa different possibilities select aagura chance increase aaguma?

Exactly!

Aana high temperature-na always better answer-nu artham illa.

Adhu just output-oda variation-ah affect pannudhu.

For example, coding-related question-ku romba high temperature use panninaa unnecessary variations varalaam.

Creative story generate panna konjam higher temperature useful-ah irukkalaam.

So, task-ku suitable-aana temperature choose panradhu important.

Temperature model-oda knowledge-ah increase pannaadhu. It only influences how the model selects its next token.

Ippo indha difference-ah Python-la paakalaam.

Namma already learn pannina NumPy library-ah use panrom.

First NumPy import panrom.

Next, logits-nu oru variable create panni three raw scores store panrom.

Adhukku apram softmax function define panrom.

Indha function input-ah logits eduthu probability values return pannum.

Ippo oru for loop use panni three different temperature values test panrom.

First temperature zero point five.

Next temperature one.

Finally temperature two.

Ovvoru temperature-kum logits-ah temperature value-la divide panni, softmax apply panrom.

Adhukku apram calculate aana probabilities-ah print panrom.

Ippo output-ah paakalaam.

Temperature zero point five-la first option-ku approximately zero point eight seven nine probability irukkum.

Temperature one-la adhu approximately zero point six nine zero.

Temperature two-la adhu approximately zero point five five zero.

Ippo output-la enna observe panreenga?

Temperature increase aagumbodhu first option-oda probability reduce aagudhu.

Other options-oda probabilities relatively increase aagudhu.

Adhaavadhu probability distribution more spread aagudhu.

Idhudhaan temperature setting-oda basic effect.

Remember, temperature probability distribution-ah change pannudhu. Actual token selection sampling method use pannumbodhu dhaan indha variation output-la reflect aagum.

Top-K and Top-P – How many choices should the model consider?

Ippo temperature purinjirukkum.

Next, Top-K and Top-P pathi paakalaam.

Imagine model next token select panna hundred possible words irukku.

Hundred words-um consider pannaama, important candidates mattum consider panna mudiyuma?

Yes!

Adhukkudhaan Top-K and Top-P use pannuvanga.

First Top-K.

Top-K equals five-na, highest probability irukkura five tokens mattum selection-ku consider pannuvom.

For example, hundred possible words irundhaalum, highest probability irukkura five options mattum model consider pannum.

So, Top-K-na fixed number of candidate tokens.

Ippo Top-P.

Top-P konjam different.

Idhula fixed number of words select panna maattom.

Instead, highest probability irukkura words-ah one by one consider pannuvom.

Andha words-oda combined probability namma set panna threshold reach aagura varaikkum candidates include aagum.

For example, Top-P value ninety percent-ah irundhaa, cumulative probability approximately ninety percent reach aagura varaikkum highest probability tokens include pannuvom.

So, Top-K fixed number of candidates use pannudhu.

Top-P cumulative probability threshold use pannudhu.

Ippo oru quick recap.

Temperature probability distribution evlo spread aaganum-nu influence pannudhu.

Top-K and Top-P endha possible tokens selection-ku consider pannanum-nu control pannudhu.

Indha settings ellam model answer generate panra style-ah influence pannum.

KV Cache – How does the model avoid repeating calculations?

Ippo namma inference process-la innum oru important optimization paakalaam.

Adhu dhaan KV cache.

Idha understand panna oru simple situation imagine pannunga.

Neenga ChatGPT-kitta oru long paragraph kudukkureenga.

Adhula neraya sentences and information irukku.

Model first indha entire input-ah process pannanum.

Indha initial input processing stage-ku prefill-nu peru.

Indha stage-la model input tokens-ku thevaiyana Key and Value information calculate pannum.

Adhukku apram model answer generate panna start pannum.

Indha process-la one token at a time generate aagum.

Indha stage-ku decoding-nu peru.

Ippo oru question.

Model already previous tokens-ku Key and Value information calculate panniduchu.

Adutha token generate pannumbodhu, andha previous calculations-ah thirumba perform panna vendiyirukkuma?

Not necessarily!

Already calculate panna Key and Value information-ah temporary memory-la store panni reuse pannalaam.

Adhukkudhaan KV cache-nu peru.

KV-na Key and Value.

Cache-na temporarily store panni later reuse panradhu.

So, KV cache previous tokens-oda Key and Value information-ah store panni, repeated calculations reduce panna help pannum.

Idhunaala token generation more efficient-ah irukka mudiyum.

Aana idhukkum oru trade-off irukku.

KV cache temporary memory use pannum.

Conversation romba long-ah irundhaa, process panna vendiya tokens increase aagum. Adhanaala KV cache memory requirement-um increase aagalaam.

So, KV cache performance improve panna help panninaalum, memory management-um important.

Website-la ulla Machine Learning course-la Probability and Probability Distributions pathina detailed explanations Module Three-la irukku. Indha LLM course-ah complete pannadhukku apram, andha module-ah check pannunga.
