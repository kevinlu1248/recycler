# Recycler
For sorting recyclables using Google AutoML. Try it out at https://recycler-mvdcj7favq-uc.a.run.app.

## Process:
I started by directly using Google Vision ML API but it gave information that was too vague to use to classify the recyclables.
It gave me information such as "bottle", or "products", so I tried fine-tuning on Xception, which was a lot more accurate 
(86% precision). Huge shoutout to Gary Thung's dataset at https://github.com/garythung/trashnet. I am planning also to 
add more from Huawei's garbage sorting competition https://competition.huaweicloud.com/information/1000007620/circumstances?track=107,
which has around 20000 images, although the majority of them don't apply to this project.
