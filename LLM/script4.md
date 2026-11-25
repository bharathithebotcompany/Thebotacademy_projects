PART FOUR – HOW DOES THE MODEL LEARN TO PREDICT WORDS?

Okay, ippo namma oru small game vilayaadalaam.

Naan oru sentence start panren.

"The sun rises in the..."

Next enna word varum?

East!

Most people-ku idhu easy-ah guess panna mudiyum.

Why?

Because namakku already language patterns and world knowledge irukku.

Language model-um massive amounts of text examples-lendhu patterns learn pannum.

Idhula oru common training method dhaan next-token prediction.

Adhaavadhu, model-kku kudukkappatta words-ku apram next enna token varalaam-nu predict panna train pannuvanga.

Ippo idha step by step understand pannalaam.

Imagine namma model-ku, "The sun rises in the" nu input kudukrom.

Model next enna varalaam-nu predict pannum.

Suppose adhu "west" nu predict pannuchu.

But namma training example-la correct word "east".

Appo model prediction and correct answer compare panni, evlo difference irukku-nu calculate pannuvanga.

Indha difference-ah measure panna loss function use pannuvanga.

Simple-ah sollanumna, model prediction evlo wrong-ah irukku-nu measure panra number dhaan loss.

Loss romba high-ah irundhaa, model prediction correct answer-lendhu distance-la irukku-nu indicate pannalaam.

Loss low-ah irundhaa, correct answer-ku model higher probability kuduthirukku-nu indicate pannalaam.

Ippo indha process-ah Python-la paakalaam.

Namma three possible answers irukku-nu assume pannuvom.

East, West and North.

Model indha moonu options-kum different scores kuduthirukku-nu imagine pannunga.

Indha raw scores-ku logits-nu peru.

Logits-na probabilities illa. Model generate panra raw numerical scores.

Ippo indha scores-ah probabilities-ah convert panna softmax use pannuvom.

Code-la first NumPy library import panrom.

Next, logits-nu oru variable create panrom.

Adhula three numerical scores store panrom.

Adhukku apram softmax-nu oru function define panrom.

Function-na oru particular task perform panna ezhudhura reusable block of code.

Indha function input-ah scores eduthu, probabilities calculate panni return pannum.

Next, probabilities-nu oru variable-la softmax result store panrom.

Adhukku apram possible words-ah oru list-la store panrom.

East, West and North.

For loop use panni ovvoru word-oda probability-ah display panrom.

Finally, correct answer East-nu assume panni, adhan probability use panni loss calculate panrom.

Inga negative log probability use panrom.

Ippo code-ah run pannalaam.

Output-la East-ku approximately zero point six five nine probability varum.

West-ku zero point two four two.

North-ku zero point zero nine nine.

And loss approximately zero point four one seven.

Paartheengala?

Model East-ku highest probability kuduthirukku.

Namma correct answer East-nu assume pannom.

Andha correct answer-ku model kudutha probability use panni loss calculate pannom.

Correct answer-ku probability high-ah irundhaa loss lower-ah irukkum.

Probability romba low-ah irundhaa loss higher-ah irukkum.

But idhu oru simplified example mattum.

Actual LLM training-la huge datasets, massive neural networks and millions or billions of parameters irukkalaam.

Ippo next question.

Model thappana prediction pannuchu-na adhu epdi improve aagum?

Idhukkaaga neural network-oda internal numerical values, adhaavadhu weights, adjust pannuvanga.

Indha weights-ah update panna gradient descent and backpropagation use pannuvanga.

Indha terms konjam technical-ah irukkalaam. So, simple-ah understand pannalaam.

Imagine neenga oru exam write panreenga.

Exam mudinjadhukku apram unga mistakes identify panni, enga improve pannanum-nu analyse panreenga.

Adhe maadhiri, model prediction-la irukkura error-ah calculate pannuvanga.

Backpropagation use panni, andha error neural network-oda different layers-ku epdi related-ah irukku-nu calculate pannuvanga.

Gradient descent use panni, loss reduce aagura direction-la weights update pannuvanga.

Indha process repeated-ah nadakkum.

Model prediction, loss calculation, gradient calculation, weight update.

Again prediction. Again loss. Again weight update.

Ippadi repeated training moolama model patterns learn pannum.

Ippo LLM training-la use panra different stages pathi paakalaam.

First, pretraining.

Pretraining-la massive amounts of text data use panni model language patterns learn pannum.

Words epdi combine aagudhu, sentences epdi form aagudhu, different types of text-la patterns epdi irukku-nu learn pannum.

Next, fine-tuning.

Fine-tuning-na already trained model-ah additional training moolama particular task or behaviour-ku adapt panradhu.

For example, general text model-ah instruction follow panra assistant-ah improve panna additional examples use pannalaam.

Supervised fine-tuning-la instructions and expected answers maadhiri examples kuduthu train pannuvanga.

Adhukku apram human preference-based training techniques-um use pannalaam.

RLHF-na Reinforcement Learning from Human Feedback.

Indha approach-la human feedback use panni model behaviour improve panna try pannuvanga.

DPO-na Direct Preference Optimization.

Idhu preferred answers and less-preferred answers maadhiri comparison data use panni model-ah optimize panna help pannum.

Indha techniques ellam same method illa. Different approaches and training objectives irukku.

Ippo basic difference clear-ah irukkanum.

Pretraining broad language capabilities develop panna help pannum.

Fine-tuning already trained model-ah particular needs-ku adapt panna help pannum.
