PART THIRTEEN – HOW DOES A MACHINE MAKE DECISIONS LIKE A HUMAN? UNDERSTANDING DECISION TREES

Imagine pannunga, neenga oru online shopping website-la mobile phone vaanga porீங்க.

Oru mobile phone select panradhukku munnaadi, unga mind-la sila questions varum.

First, budget evvalavu?

Adhukku apram, camera quality mukkiyamaa? Battery life mukkiyamaa?

Gaming-ku use panna porீங்களா? Illa normal usage-ku mattum dhaana?

Indha questions-oda answers-ah base panni, neenga oru mobile phone select pannuveenga.

Adhaavathu, ovvoru question-kum answer kandupidichu, step by step-ah oru final decision-ku varuveenga.

Ippo idhe maadhiri oru decision-making process-ah computer follow panna mudiyumaa?

Definitely mudiyum.

Machine Learning-la indha maadhiri questions and conditions use panni decisions edukka help panra oru important algorithm dhaan Decision Tree.

Namma previous lessons-la Machine Learning models data-la irukkura patterns-ah learn panni predictions edukkuradhu pathi paathom.

Ippo andha predictions-ah oru series of questions moolama model epdi arrive aagudhu-nu understand pannalaam.

WHAT IS A DECISION TREE?

Decision Tree-na data-la irukkura patterns-ah analyse panni, a series of questions and conditions moolama prediction edukka use panra Machine Learning algorithm.

Idhoda structure oru tree maadhiri irukkum.

Oru starting point-la irundhu questions begin aagum.

Ovvoru question-kum answer kidaikkumbodhu, adutha question-ku move aaguvom.

Ippadi different questions-ah follow pannittu, kadaisila oru final decision-ku varuvom.

Indha structure tree maadhiri irukkuradhunaala idhukku Decision Tree-nu peru vandhuduchu.

Decision Tree-la questions mattum illaama, ovvoru question-oda possible answers and final predictions-um structured-ah arrange pannappattirukkum.

Idha purinjikka oru simple example eduthukalaam.

Oru bank customer-ku loan approve pannalaamaa illaiyaa-nu decide panna vendiyirukku-nu imagine pannunga.

Bank-kitta previous loan applications-oda data irukku.

Indha data-la customer income, credit score, existing loan details and previous repayment history maadhiri information irukku.

Indha information-ah use panni Decision Tree model train pannalaam.

Training mudinja apram, pudhu customer loan apply pannumbodhu, model different questions and conditions-ah follow panni Loan Approve illa Reject-nu prediction edukka mudiyum.

Aana indha tree structure-la irukkura different parts enna?

Adha next-ah paakalaam.

UNDERSTANDING THE STRUCTURE OF A DECISION TREE

Decision Tree-la mainly moonu important components irukku.

Root Node, Decision Node and Leaf Node.

First, Root Node.

Root Node-na Decision Tree-oda starting point.

Tree-la first question inga dhaan irukkum.

Namma loan approval example-la, customer-oda Credit Score seven hundred-kku mela irukkaa-nu first question kekkalaam.

Indha first question irukkura starting point dhaan Root Node.

Next, Decision Node.

Decision Node-na tree-la further decisions edukka use panra intermediate question points.

Oru question-ku answer kidaichadhukku apram, innoru question kekka vendiya situation irundhaa, andha question Decision Node-la irukkum.

For example, customer-oda Credit Score seven hundred-kku mela irundhaa, next customer income sufficient-ah irukkaa-nu check pannalaam.

Indha question oru Decision Node.

Finally, Leaf Node.

Leaf Node-na Decision Tree-oda final output or prediction.

Inga vandhutta, tree-la further questions edhuvum irukkaadhu.

Namma loan example-la final output Loan Approved illa Loan Rejected-ah irukkalaam.

Indha final decision irukkura point dhaan Leaf Node.

So, Root Node-na starting question.

Decision Node-na additional questions.

Leaf Node-na final prediction.

Indha moonu components-um serndhu oru complete Decision Tree structure-ah form pannum.

HOW DOES A DECISION TREE MAKE A PREDICTION?

Ippo tree-oda structure purinjikittom.

Aana model indha questions-ah epdi use panni prediction edukkuvudhu?

Namma loan approval example-ah continue pannalaam.

Oru new customer loan apply panraaru-nu vechukkonga.

Model first Root Node-la irukkura question-ah check pannum.

Customer-oda Credit Score seven hundred-kku mela irukkaa?

Answer Yes-na, tree-oda Yes branch-la move aagum.

Answer No-na, No branch-la move aagum.

Ippo Yes branch-la customer income sufficient-ah irukkaa-nu next question irukkalaam.

Adhukkum answer Yes-na, next branch-ku move aagum.

Indha process-la ovvoru condition-um check pannittu, model final-ah oru Leaf Node-ah reach pannum.

Andha Leaf Node-la irukkura prediction dhaan model-oda output.

Inga mukkiyamaana vishayam enna-na, model every time same questions-ah random-ah kekkala.

Training time-la learn panna Decision Tree structure-ah follow pannudhu.

Pudhu input varumbodhu, andha input-oda values-ah tree-la irukkura conditions-oda compare panni, correct path-la travel pannum.

Idhudhaan Decision Tree prediction process.

HOW DOES A MODEL BUILD A DECISION TREE?

Ippo Decision Tree epdi prediction edukkuvudhu-nu purinjikittom.

Aana oru important question irukku.

Tree-la first question enna irukkanum?

Second question enna irukkanum?

Endha Feature-ah first use pannanum?

Endha Feature-ah next use pannanum?

Indha questions-ah model epdi decide pannudhu?

Decision Tree training time-la dataset-la irukkura different Features-ah analyse pannum.

Ovvoru Feature-um data-ah useful-ah separate panna help pannudha-nu evaluate pannum.

Andha evaluation base panni, best question-ah select panna try pannum.

Idha purinjikka innoru example eduthukalaam.

Oru school-kitta students exam-la Pass aaguraangalaa illa Fail aaguraangalaa-nu predict panna dataset irukku-nu imagine pannunga.

Indha dataset-la students-oda Study Hours, Attendance and Previous Exam Scores maadhiri Features irukku.

Training data-la ovvoru student-um Pass illa Fail-nu already label pannappattirukkaanga.

Ippo model indha Features-la edhu students-ah Pass and Fail categories-ah better-ah separate pannudhu-nu analyse pannum.

Study Hours use panni split pannumbodhu, rendu groups-layum Pass and Fail students mix aaguraangalaa?

Attendance use panni split pannumbodhu, categories innum clear-ah separate aagudha?

Previous Exam Scores use panni split pannumbodhu, useful separation kidaikkudha?

Ippadi different possibilities-ah evaluate pannittu, data-ah best-ah separate panna help panra Feature and condition-ah model select pannum.

Indha process dhaan Decision Tree-oda Splitting.

WHAT IS DATA SPLITTING?

Splitting-na dataset-ah oru condition base panni different groups-ah divide panradhu.

For example, Study Hours four hours-kku mela irukkaa-nu model oru condition create pannalaam.

Four hours-kku mela irukkura students oru group-la pogalaam.

Four hours illa adhukku keezha irukkura students innoru group-la pogalaam.

Ippo indha rendu groups-layum students-oda Pass and Fail labels-ah model analyse pannum.

Oru group-la mostly Pass students irundhaa, innoru group-la mostly Fail students irundhaa, indha split useful-ah irukkalaam.

Aana ella splits-um equally useful-ah irukkaadhu.

Oru Feature-ah use panni split pannumbodhu, rendu groups-layum Pass and Fail students almost equal-ah mix aagirundhaa, andha split useful information-ah provide pannama irukkalaam.

Adhanaala model best split-ah select panna oru measurement use pannum.

Adhukkuthaan Impurity and Information Gain maadhiri concepts use aagudhu.

WHAT IS IMPURITY IN A DECISION TREE?

Impurity-na oru group of data-la different categories evvalavu mix aagirukku-nguradha measure panra concept.

Simple-ah sollanumna, oru group-la irukkura data points ellam same category-ah irundhaa, andha group pure-ah irukku-nu sollalaam.

Oru group-la different categories mix aagirundhaa, andha group impurity adhigama irukkum.

Namma Pass and Fail example-ah continue pannalaam.

Oru group-la ten students irukkaanga-nu vechukkonga.

Andha ten students-um Pass aagirukkaanga.

Inga ore category dhaan irukku.

So, indha group completely pure.

Innoru group-la five students Pass and five students Fail aagirukkaanga-nu vechukkonga.

Inga rendu categories-um equal-ah mix aagirukku.

So, indha group-la impurity adhigam.

Decision Tree-oda main objective enna-na, data-ah split pannumbodhu different categories-ah mudinja alavukku separate panna try panradhu.

Adhaavathu, impurity-ah reduce panna try pannum.

Indha impurity-ah calculate panna different mathematical methods irukku.

Adhula common-ah use aagura rendu methods dhaan Gini Impurity and Entropy.

UNDERSTANDING GINI IMPURITY

First, Gini Impurity pathi paakalaam.

Gini Impurity-na oru group-la different categories evvalavu mixed-ah irukku-nguradha calculate panra measurement.

Idhu zero-lendhu higher values varaikkum range aagum.

Gini Impurity zero-na andha group-la ore category mattum dhaan irukku.

Adhaavathu, group completely pure-ah irukku.

Gini Impurity higher-ah irundhaa, different categories adhigama mix aagirukku-nu artham.

Idhoda formula:

Gini Impurity equals one minus the sum of each class probability squared.

Ippo indha formula-ah simple-ah understand pannalaam.

Oru group-la ten students irukkaanga.

Adhula eight students Pass. Rendu students Fail.

Pass probability zero point eight.

Fail probability zero point two.

Ippo rendu probabilities-ah square panni add pannanum.

Zero point eight squared equals zero point six four.

Zero point two squared equals zero point zero four.

Rendaiyum add panninaa zero point six eight.

Adhai one-lendhu subtract panninaa, Gini Impurity zero point three two.

Ippadi oru group-la categories evvalavu mixed-ah irukku-nguradha Gini Impurity moolama measure pannalaam.

Decision Tree different splits-ah evaluate pannumbodhu, andha splits-kku apram groups-oda impurity evvalavu reduce aagudhu-nu paakkum.

Lower impurity kidaikkura split useful-ah irukkalaam.

UNDERSTANDING ENTROPY AND INFORMATION GAIN

Gini Impurity maadhiriye, Entropy-um data-la irukkura uncertainty or mixture-ah measure panna use aagura concept.

Simple-ah sollanumna, oru group-la different categories evvalavu mixed-ah irukku-nguradha Entropy measure pannum.

Entropy zero-na group completely pure-ah irukku.

Different categories mix aagumbodhu Entropy increase aagum.

Decision Tree-la Entropy use panni split quality-ah evaluate pannalaam.

Ippo Information Gain-na enna?

Information Gain-na oru split panna munnadi irundha impurity or uncertainty compare pannumbodhu, split panna apram evvalavu reduce aagudhu-nguradha measure panradhu.

For example, namma dataset-la Pass and Fail students ellarum mix-ah irukkaanga.

Ippo Study Hours base panni split pannrom.

Split panna apram, rendu groups-layum Pass and Fail students better-ah separate aagittaanga-nu vechukkonga.

Appo uncertainty reduce aagiyirukku.

Indha reduction dhaan Information Gain.

Higher Information Gain kidaikkura split, andha decision point-ku useful-ah irukkalaam.

So, Gini Impurity and Entropy data groups evvalavu mixed-ah irukku-nguradha measure panna help pannum.

Information Gain, oru split uncertainty-ah evvalavu reduce pannudhu-nguradha measure panna help pannum.

Decision Tree algorithms indha maadhiri measurements-ah use panni suitable splits-ah select pannum.

WHEN DOES A DECISION TREE STOP GROWING?

Ippo model questions select panni data-ah split pannudhu-nu purinjikittom.

Aana oru tree evvalavu dhaan grow aagum?

Ovvoru split-kum apram, model further questions create pannalaam.

Ippadi continue aagitte ponaa, tree romba perusa maaralaam.

Training data-la irukkura almost every small detail-ah separate panna try pannalaam.

Idhanaala tree unnecessarily complex-ah aagura possibility irukku.

So, Decision Tree grow aaguradhukku sila stopping conditions use pannalaam.

For example, tree-oda maximum depth-ah limit pannalaam.

Maximum Depth-na Root Node-lendhu Leaf Node varaikkum tree evvalavu levels grow aagalaam-ngura limit.

Maximum depth three-nu set panninaa, tree three levels-kku mela grow aagaama control pannalaam.

Innor condition Minimum Samples Split.

Idhu oru node-ah further split panna minimum evvalavu data points irukkanum-nguradha specify pannum.

For example, oru node-la five data points mattum irundhaa, adhai further split pannaama stop pannalaam.

Innor condition Minimum Samples Leaf.

Idhu ovvoru final Leaf Node-layum minimum evvalavu data points irukkanum-nguradha control pannum.

Indha settings use panni tree-oda growth-ah control pannalaam.

Ippadi tree romba complex-ah aagama manage panra process-ku Pruning-um use aagum.

Pruning-na already grow aana Decision Tree-la unnecessary branches-ah remove panni tree-ah simpler-ah maathura process.

Idhoda goal tree-oda unnecessary complexity-ah reduce panni, new data-layum better-ah perform panna help panradhu.

CAN DECISION TREES BE USED FOR REGRESSION?

Ippo varaikkum namma Pass and Fail, Loan Approval and Rejection maadhiri categories-ah predict panra examples use pannom.

Aana Decision Tree Classification-ku mattum dhaana use aagum?

Illa.

Decision Trees Regression problems-kum use pannalaam.

Classification Decision Tree-na final-ah oru category-ah predict pannum.

Regression Decision Tree-na final-ah oru numerical value-ah predict pannum.

For example, house price predict panra problem-ah eduthukalaam.

Model house size, location and number of rooms maadhiri information-ah analyse pannum.

Indha Features base panni data-ah different groups-ah split pannum.

Final-ah oru Leaf Node reach aagumbodhu, andha group-la irukkura training examples-oda average house price maadhiri numerical value-ah prediction-ah provide pannalaam.

So, Decision Tree-oda structure similar-ah irundhaalum, final output problem-ah poruththu maarum.

Classification-na category.

Regression-na numerical value.

ADVANTAGES OF DECISION TREES

Ippo Decision Tree epdi work aagudhu-nu detailed-ah paathom.

Aana Machine Learning-la pala algorithms irukkumbodhu, Decision Tree-ah yen use pannanum?

Decision Tree-oda first advantage, idhai understand panradhu relatively easy.

Oru model prediction edukkuradhukku endha questions and conditions-ah follow pannuchu-nu tree structure-ah paathale purinjikka mudiyum.

Second, numerical and categorical Features rendu type data-vayum handle panna mudiyum.

Third, complex mathematical calculations-ah manually define pannaama, model training time-la useful splits-ah learn pannikkum.

Fourth, Classification and Regression rendu problems-kum Decision Trees use pannalaam.

Indha reasons-naala Decision Trees Machine Learning-la widely used algorithms-la onnu.

LIMITATIONS OF DECISION TREES

Aana Decision Trees-ku advantages mattum illa. Sila limitations-um irukku.

First, Decision Trees easily Overfit aagura possibility irukku.

Tree romba deep-ah grow aagi, training data-la irukkura unnecessary details-ah learn panniduchu-na, new data-la performance reduce aagalaam.

Second, small changes in training data kooda tree structure-ah change pannalaam.

Oru dataset-la train panna tree-oda questions and branches, slightly different dataset-la vera maadhiri irukkalaam.

Third, tree romba complex-ah aagumbodhu, adhai understand panradhu difficult-ah maaralaam.

Fourth, Decision Tree training data-la irukkura patterns-ah base panni decisions edukkuradhu naala, biased or incomplete training data irundhaa predictions-um affect aagalaam.

Adhanaala Decision Tree use pannumbodhu, tree-oda depth, splitting conditions and evaluation performance-ah properly monitor pannanum.

Ippo namma Decision Tree-na enna, Root Node, Decision Node, Leaf Node epdi work aagudhu, data epdi split aagudhu, Gini Impurity, Entropy and Information Gain epdi help pannudhu-nu paathom.

Decision Tree oru model-ah questions and conditions moolama predictions edukka vaikkudhu.

Aana sila real-world problems-la single Decision Tree mattum use pannaama, pala models-oda predictions-ah combine panni innum better results achieve panna mudiyum.

Appadi multiple Machine Learning models onna serndhu work pannumbodhu enna nadakkum?

Adutha part-la, multiple models epdi serndhu predictions improve pannudhu-nu paakalaam.