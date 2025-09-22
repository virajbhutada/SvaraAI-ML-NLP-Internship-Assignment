# Part C – Short Answer (Reasoning)


**1. If you only had 200 labeled replies, how would you improve the model without collecting thousands more?**

With a limited labeled dataset, I would apply data augmentation techniques such as paraphrasing, back-translation, and synonym replacement to increase data diversity. Leveraging transfer learning with pre-trained transformer models like DistilBERT allows the model to benefit from contextual knowledge, improving performance even with small datasets. Additionally, semi-supervised learning or active learning strategies can further enhance model accuracy without requiring large amounts of new labeled data.


**2. How would you ensure your reply classifier doesn’t produce biased or unsafe outputs in production?**

To mitigate bias and unsafe outputs, I would evaluate the model across diverse datasets that represent all demographic and linguistic groups. Implementing content filters, human-in-the-loop verification, and monitoring predictions continuously ensures that potentially harmful or biased outputs are detected and corrected. Regular audits, retraining, and updating the model with feedback are crucial to maintain fairness and safety over time.


**3. Suppose you want to generate personalized cold email openers using an LLM. What prompt design strategies would you use to keep outputs relevant and non-generic?**

I would provide structured context in the prompt, including recipient details such as name, company, industry, and role. Incorporating examples of high-quality, domain-specific openers and specifying the desired tone, style, and formality level helps the LLM produce outputs that are relevant, personalized, and engaging. Iteratively refining prompts based on output evaluation further ensures non-generic, high-quality results.
