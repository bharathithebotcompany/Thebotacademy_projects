# PART TWO – HOW DOES A COMPUTER READ OUR SENTENCE?

Okay, ippo naan computer-kitta oru sentence kudukkuren.

"Today I am learning Artificial Intelligence."

Namma indha sentence-ah paathaa easy-ah read panniduvom.

Aana computer epdi idha handle pannum?

Computer-ku English theriyum-nu namma solla mudiyadhu. Computers fully numbers-ah dhaan process pannum.

So, namma kudukkura sentence-ah computer process panna suitable-aana format-ku maathanum.

Idha oru simple example-la paakalaam.

Namma school-la attendance edukkarappo students-oda names irukkum. Aana school system-la each student-ku oru unique roll number-um irukkum.

Name-ah identify panna use pannuvom. Roll number-ah system-la identify panna use pannuvom.

Adhe maadhiri, language model-kum words-ah identify panna numerical identification numbers use pannuvanga.

Indha process-la first varra concept dhaan tokenization.

Tokenization-na namma sentence-ah small pieces-ah split panradhu.

Indha pieces-ku tokens-nu peru.

For example, "I love learning Python" nu oru sentence eduthukonga.

Idha tokenizer, I, love, learning, Python-nu separate pieces-ah split pannalaam.

Inga oru important point.

Oru token-na always oru complete word-nu artham illa.

Sometimes oru long word multiple pieces-ah split aagum.

Why is that useful?

Imagine English-la irukkura ella words-um separate-ah store pannanumna romba periya list thevaippadum.

Adhukku badhila, words-la repeat aagura smaller pieces use panninaa, model-ku language-ah represent panradhu easier aagum.

Idhukkudhaan subword tokenization use pannuvanga.

B P E and WordPiece maadhiri methods indha smaller pieces-ah create panna help pannum.

Ippo andha algorithms-oda details-ku pogama, namma actual tokenizer output paakalaam.

Python therinjavangalukku indha code easy-ah irukkum. Python romba pudhusaa irukkura students-kooda parava illa. Naan ovvoru line-ah explain panren.

First, namma Transformers-nu oru Python library use panrom.

Indha library-la already trained models and tokenizers use panna facilities irukku.

Indha library-ah install panna terminal-la, P I P install Transformers, nu type pannanum.

Inga P I P-na Python package install panna use panra command.

Next, code-la Transformers library-lendhu AutoTokenizer-nu oru component-ah import panrom.

Adhukku apram, AutoTokenizer dot from underscore pretrained nu oru method call panrom.

Opening bracket, double quote, G P T two, double quote, closing bracket.

Indha line enna pannudhu-na, G P T two model-oda tokenizer-ah load pannudhu.

Next line-la sentence-nu oru variable create panrom.

Equals symbol use panni, double quotes-kulla, I love learning Python, nu sentence assign panrom.

Adhukku apram tokens-nu oru variable create panni, tokenizer dot tokenize method-ku namma sentence-ah pass panrom.

Opening bracket, sentence, closing bracket.

Indha method namma sentence-ah smaller pieces-ah split pannum.

Finally, print method use panni original sentence, tokens and token count display panrom.

Token count calculate panna length method use panrom.

Length method-kulla tokens variable-ah pass panrom.

Ippo indha program-ah run pannalaam.

Output-la original sentence display aagum.

Adhukku keezha tokens display aagum.

And finally, total token count display aagum.

Indha example-la tokenizer five tokens create pannirukku.

Remember, tokenizer version and model poruththu exact output change aagalaam. Every tokenizer-um same way-la sentence-ah split pannum-nu illa.

Okay, ippo namakku tokens kidaichiduchu.

Aana computer-ku numerical values venum-nu sonnom la?

Adhukkaaga ovvoru token-kum oru number assign panniruppanga.

Andha number-ku token ID-nu peru.

Ippo adhayum paakalaam.

Namma code-la token underscore I Ds-nu oru variable create panrom.

Equals symbol use panni, tokenizer dot encode method call panrom.

Opening bracket, sentence, closing bracket.

Indha method sentence-ah token IDs-ah convert pannum.

Next, print method use panni token IDs display panrom.

Adhukku apram number of IDs display panna, length method use panrom.

Ippo run panninaa, ovvoru token-kum oru number output-la varum.

Indha number andha token-ah model vocabulary-la identify panna use aagum.

Oru important difference.

Token ID-na oru identification number. Adhula word-oda meaning store aagirukkunnu artham illa.

Appo meaning epdi represent aagum?

Adhukkudhaan next concept, Embeddings.

Imagine unga school-la students ellarukkum roll numbers irukku.

Roll number vechu student-ah identify pannalaam.

Aana andha student-oda height, marks, interests, performance pathi therinjukka roll number mattum podhaadhu.

Adhukkaaga additional information venum.

Adhe maadhiri, token ID mattum vechu model-ku useful language representation kidaikkaadhu.

So, model ovvoru token ID-ah oru collection of numbers-ah maathum.

Indha collection of numbers-ku embedding vector-nu peru.

Simple-ah sollanumna, token ID is the identification number. Embedding is the numerical representation that the model processes.

Indha vectors-la irukkura relationships-ai training moolama model learn pannum.

Inga namma website la ulla Machine Learning course-la vara vectors and matrices pathi-na oru detailed concept varum, after this course antha course poi padichi paarunga.

Ippo namma text numbers-ah maari, model process panna ready-aagiduchu.

Next, indha information-ah model epdi understand panna try pannudhu-nu paakalaam.
