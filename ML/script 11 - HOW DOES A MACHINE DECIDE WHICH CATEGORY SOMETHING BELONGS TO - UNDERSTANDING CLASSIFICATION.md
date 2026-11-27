PART ELEVEN – HOW DOES A MACHINE DECIDE WHICH CATEGORY SOMETHING BELONGS TO? UNDERSTANDING CLASSIFICATION

Imagine pannunga, oru online shopping website-ku daily thousands of customer support messages varudhu.

Adhula sila customers payment problem pathi message panniruppaanga. Sila customers product delivery pathi ketiruppaanga. Innum sila customers account-related problems pathi contact panniruppaanga.

Ippo ovvoru message-ah open panni, adhu endha department-ku belong aagudhu-nu employees manually decide panna vendiyirundhaa evvalavu time aagum?

Adhanaala indha maadhiri applications-la Machine Learning models use panni, incoming messages-ah analyse senju, correct category-ku automatically assign pannalaam.

Aana oru message payment problem-ah, delivery problem-ah, illa account problem-ah-nu computer epdi decide pannudhu?

Andha message-la irukkura words-ah mattum paakkudha? Illa sentence-oda meaning and previous messages-la irundha patterns-ah kooda consider pannudha?

Indha maadhiri oru input-ah analyse panni, adhu endha category-ku belong aagudhu-nu predict panra Machine Learning approach dhaan Classification.

Previous lesson-la Regression use panni numerical values-ah epdi predict panradhu-nu paathom.

Ippo numerical value predict panradhukku badhila, oru category-ah epdi predict panradhu-nu understand pannalaam.

WHAT IS CLASSIFICATION?

Classification-na input data-ah analyse panni, adhu endha predefined category-ku belong aagudhu-nu predict panra Machine Learning approach.

Inga Category-na oru group illa class.

For example, oru medical report-la irukkura information-ah base panni, oru particular condition irukka illaiya-nu classify panradhu.

Bank transaction suspicious-ah illa normal-ah-nu identify panradhu.

Customer review positive-ah illa negative-ah-nu identify panradhu.

Indha examples-la model oru exact numerical value-ah predict panna try pannala.

Adhukku badhila, input endha category-la varudhu-nu predict pannudhu.

Idhudhaan Classification-oda basic idea.

Namma customer support message example-ah thirumbi eduthukalaam.

Oru customer, "En payment successful-nu kaamikudhu, aana order confirm aagala" appadinu message anuppuraaru-nu vechukkonga.

Indha message-ah analyse panni, Payment Issue category-ku assign pannalaam.

Innoru customer, "En order innum delivery aagala" appadinu message anuppinaa, adhai Delivery Issue category-ku assign pannalaam.

Inga model message-la irukkura information-ah analyse panni, suitable category-ah predict pannudhu.

Training time-la model-ku already categories assign pannappatta pala messages examples-ah kuduppom.

Andha examples-la irukkura patterns-ah model learn pannum.

Training mudinja apram, pudhu message vandhaa, adhai analyse panni suitable category-ah predict pannum.

UNDERSTANDING BINARY CLASSIFICATION

Classification-la different types irukku.

First, Binary Classification pathi paakalaam.

Binary-na rendu.

So, Binary Classification-na oru input-ah rendu possible categories-la edhavadhu oru category-ku assign panradhu.

For example, bank transaction Fraud-ah illa Normal-ah-nu classify pannalaam.

Oru customer loan application Approve pannalaam illa Reject pannalaam-nu classify pannalaam.

Oru medical test result Positive-ah illa Negative-ah-nu classify pannalaam.

Inga model-ku rendu possible outcomes dhaan irukku.

Adhanaala indha problems Binary Classification-ku examples.

Ippo oru simple situation-ah imagine pannunga.

Oru bank-kitta thousands of previous transactions irukku.

Adhula sila transactions Fraud-nu identify pannappattirukku. Matha transactions Normal-nu identify pannappattirukku.

Indha previous transactions-la irukkura information-ah use panni model train aagum.

Transaction amount, transaction time, location and spending pattern maadhiri features-ah analyse pannalaam.

Training mudinja apram, pudhu transaction vandhaa, model adhai analyse panni Fraud illa Normal-nu predict pannum.

Aana model-ku indha decision epdi varudhu?

Adha purinjikka Probability Score and Classification Threshold pathi therinjikkanum.

HOW DOES A MODEL USE PROBABILITY TO CLASSIFY?

Namma previous lesson-la Probability pathi detail-ah paathom.

Oru event nadakkura possibility-ah Probability represent pannum-nu understand pannom.

Classification models-la sila algorithms ovvoru category-kum Probability Score generate pannum.

For example, oru bank transaction-ah analyse pannumbodhu, model Fraud category-ku zero point eight five probability-um, Normal category-ku zero point one five probability-um assign pannudhu-nu vechukkonga.

Idha percentage-la sonnaa, Fraud-ku eighty-five percent, Normal-ku fifteen percent.

Indha scores-ah compare panni, model Fraud category-ah select pannalaam.

Inga oru important point irukku.

Indha Probability Score-na model-oda estimate dhaan. Adhu kandippa correct-nu guarantee illa.

Model training data-la learn panna patterns-ah base panni indha score generate pannum.

Innoru transaction-ku Fraud probability zero point three and Normal probability zero point seven-ah irukkalaam.

Appo model Normal category-ah select pannalaam.

Ippadi category-wise Probability Scores generate panni, suitable category-ah select panradhu Classification-la common-ah use aagura approach.

Aana ellaa Classification models-um probability-ah same method-la calculate pannum-nu solla mudiyadhu.

Sila algorithms direct-ah probability scores provide pannum. Innum sila algorithms probability illaadha decision scores or other outputs-ah generate pannalaam.

Ippo indha Probability Score irukku. Aana endha point-la model oru transaction-ah Fraud-nu decide pannum?

Adhukkuthaan Classification Threshold use aagudhu.

Threshold-na oru decision edukka model use panra cutoff value.

For example, Fraud probability fifty percent-ah threshold-ah set pannirukkom-nu vechukkonga.

Model-oda Fraud probability fifty percent-kku mela irundhaa, transaction-ah Fraud-nu classify pannalaam.

Fifty percent-kku keezha irundhaa, Normal-nu classify pannalaam.

Ippo oru transaction-ku Fraud probability eighty-five percent-ah irukku.

Adhu fifty percent threshold-ah vida adhigam. So, model adhai Fraud-nu classify pannum.

Aana threshold-ah change panna mudiyum.

For example, bank fraud transactions-ah miss pannakoodaadhu-ngura situation-la, lower threshold use pannalaam. Appo more transactions review-kku select aagalaam. Aana genuine transactions-um mistake-ah Fraud-nu flag aagura possibility irukku.

Higher threshold use panninaa, Fraud-nu classify panradhukku stronger evidence thevaippadum. Aana sila actual fraud transactions miss aagalaam.

So, threshold select panradhu application-oda requirement-ah poruththu maarum.

Idhu dhaan Probability Score and Threshold use panni Binary Classification-la decision edukka oru common approach.

WHAT IS A DECISION BOUNDARY?

Ippo model probability use panni category select panradhu purinjikittom.

Aana model categories-ah separate panra concept-um irukku.

Adhudhaan Decision Boundary.

Decision Boundary-na different categories-ku belong aagura data points-ah separate panna model learn panra boundary.

Idha purinjikka oru simple example eduthukalaam.

Oru college-la students-oda study hours and exam scores details irukku-nu imagine pannunga.

Indha data-ah use panni students Pass aaguraangalaa illa Fail aaguraangalaa-nu predict panna model train panrom.

Inga study hours oru Feature. Exam score innoru Feature-ah eduthukalaam.

Graph-la study hours-ah X-axis-la represent pannalaam. Exam score-ah Y-axis-la represent pannalaam.

Previous students-oda data points-ah graph-la mark panninaa, sila points Pass category-la irukkum. Matha points Fail category-la irukkum.

Ippo model indha rendu categories-oda patterns-ah analyse panni, avangalai separate panna oru boundary-ah learn panna try pannum.

Andha boundary-oda oru side-la irukkura data points Pass category-ah classify aagalaam.

Innoru side-la irukkura data points Fail category-ah classify aagalaam.

Indha separation-ah Decision Boundary-nu solluvom.

Inga oru important point irukku.

Real-world problems-la Decision Boundary straight line-ah mattum irukkanum-nu avasiyam illa.

Data-la irukkura pattern and algorithm-ah poruththu, adhu straight line-ah, curved line-ah, illa innum complex shape-ah irukkalaam.

Mukkiyama, pudhu data point endha category-la varudhu-nu decide panna model indha boundary-ah use pannalaam.

UNDERSTANDING MULTICLASS CLASSIFICATION

Ippo rendu categories irukkura Binary Classification pathi paathom.

Aana ella problems-layum rendu categories mattum irukkaadhu.

For example, oru image-la irukkura animal-ah identify pannanum-nu imagine pannunga.

Andha image Dog-ah irukkalaam, Cat-ah irukkalaam, illa Bird-ah irukkalaam.

Inga moonu possible categories irukku.

Idhu Multiclass Classification.

Multiclass Classification-na oru input-ah two-kku adhigamaana categories-la edhavadhu oru category-ku assign panra approach.

For example, handwritten digit recognition-la zero-lendhu nine varaikkum irukkura numbers-la edhu image-la irukku-nu model identify pannum.

Inga total ten possible categories irukku.

Adhe maadhiri, news articles-ah Sports, Politics, Technology and Entertainment-nu classify pannalaam.

Oru customer support message-ah Billing, Technical Support, Account Issue and General Enquiry-nu classify pannalaam.

Indha situations-la model multiple categories-la edhu suitable-nu predict pannum.

Ippo handwritten digit recognition example-ah eduthukalaam.

Oru handwritten image model-kku input-ah kudukkurom-nu vechukkonga.

Model andha image-ah analyse panni, zero-lendhu nine varaikkum irukkura different categories-kku scores generate pannalaam.

For example, andha image Three-ah irukka chance adhigam-nu model estimate pannudhu.

Three category-ku highest score irundhaa, model Three-nu predict pannalaam.

Inga oru clarification.

Indha maadhiri highest Probability Score-ah select panradhu probability output provide panra models-la use pannalaam. Aana ellaa classification algorithms-um probability scores-ah generate pannum-nu avasiyam illa.

Binary Classification-la rendu categories irundhadhu.

Multiclass Classification-la rendu-kku adhigamaana categories irukkum.

Idhudhaan rendu approach-ukkum irukkura main difference.

HOW DOES CLASSIFICATION LEARN FROM DATA?

Ippo Classification-na enna, Binary and Multiclass Classification-na enna-nu purinjikittom.

Aana model indha categories-ah epdi learn pannudhu?

Namma customer support message example-ah thirumbi eduthukalaam.

First, nammakitta previous customer messages-oda dataset irukku.

Ovvoru message-layum customer type panna words, sentence structure and other information irukkum.

Adhoda andha message Payment Issue-ah, Delivery Issue-ah, illa Account Issue-ah-nu label-um irukkum.

Inga message details ellam Features.

Payment Issue, Delivery Issue, Account Issue-ngura categories Labels.

Training time-la model Features and Labels rendu peraiyum analyse pannum.

Different messages-la enna patterns irukku-nu identify panna try pannum.

For example, payment-related messages-la transaction, refund, payment failed maadhiri words irukkalaam.

Delivery-related messages-la order, shipment, tracking and delivery maadhiri words irukkalaam.

Account-related messages-la login, password and account access maadhiri words irukkalaam.

Indha maadhiri patterns-ah model training examples moolama learn pannum.

Training mudinja apram, pudhu message varumbodhu, adhu already dataset-la irundha message-ah irukkanum-nu avasiyam illa.

Model learn panna patterns-ah use panni, andha pudhu message endha category-ku belong aagudhu-nu predict pannum.

Aana training data correct-ah label pannappattirukkanum.

Training examples-la mistakes irundhaa, model-um wrong patterns-ah learn panna chance irukku.

Adhanaala Classification-ku data quality romba mukkiyam.

Classification-ku different algorithms-um irukku.

For example, Logistic Regression, Decision Tree, K-Nearest Neighbors, Naive Bayes and Support Vector Machine.

Indha algorithms ellam data-la irukkura patterns-ah different methods-la analyse panni categories-ah predict pannum.

Oru algorithm probability-based approach use pannalaam. Innoru algorithm distance or decision rules maadhiri concepts-ah use pannalaam.

Endha algorithm suitable-nguradhu namma problem, dataset and requirements-ah poruththu decide aagum.

Indha algorithms-la Decision Tree-um oru important method.

Adha pathi namma later lesson-la detailed-ah paaka porom.

REGRESSION VS CLASSIFICATION

Ippo Regression and Classification rendu approaches-um paathirukkom.

Indha rendu methods-ukkum irukkura difference-ah oru simple comparison moolama understand pannalaam.

Suppose namma house details-ah use panni house price predict panrom.

Output forty lakh, fifty lakh, sixty lakh maadhiri numerical value-ah irukkum.

Idhu Regression problem.

Aana adhe house details-ah use panni, house Affordable-ah illa Expensive-ah-nu category predict panrom-nu vechukkonga.

Inga output oru category.

Idhu Classification problem.

Adhe maadhiri, customer next month evvalavu spend pannuvaaru-nu predict panradhu Regression.

Customer product purchase pannuvaaraa illa maattaaraa-nu predict panradhu Binary Classification.

So, problem-la namakku thevaiyaana output enna-nguradha base panni Regression-ah illa Classification-ah select pannanum.

Numerical value thevai-na Regression.

Category thevai-na Classification.

WHERE IS CLASSIFICATION USED IN THE REAL WORLD?

Classification namma daily use panra pala applications-la work aagudhu.

Email services Spam and Genuine emails-ah separate pannudhu.

Banking systems suspicious transactions-ah identify panna Classification models-ah use pannalaam.

Healthcare applications medical information-ah analyse panni, different risk categories-ah identify panna use pannalaam.

Online shopping platforms customer reviews Positive-ah, Negative-ah, illa Neutral-ah-nu classify pannalaam.

Customer support systems incoming messages-ah analyse panni, endha department handle pannanum-nu category assign pannalaam.

Indha applications ellathulayum input data-ah analyse panni, suitable category-ah predict panradhu dhaan main objective.

Ippo Classification moolama oru input endha category-ku belong aagudhu-nu model epdi predict pannudhu-nu paathom.

Aana oru model Fraud-nu predict pannudhu-nguradhunaala mattum adhu correct-ah work aagudhu-nu solla mudiyadhu.

Model evvalavu predictions correct-ah pannudhu, evvalavu mistakes pannudhu, different categories-la performance epdi irukku-nu measure pannanum.

Adhukkuthaan model evaluation metrics use aagudhu.

Adutha lesson-la, namma train panna Machine Learning model-oda performance-ah epdi measure panradhu-nu paakalaam.