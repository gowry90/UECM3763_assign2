UECM3763 Computational Finance (Assignment #2)
========================================================
--------------------------------------------------------

DEADLINES: 
- This assignment will contribute to 5 marks of the coursework.
- Assignment submission: 27/7/2015 (Monday) by 12:00 noon.
- Peer Reviews: 3/8/2015 (Monday) by 12:00 noon.

**All deadlines are final and no extensions are allowed.** Delay in submission of the assigments will delays the peer review process. Thus a penalty of 1 mark per day will be imposed for one day late in submission of assignment. Each student will need to review two peers. No mark will be awarded if a student failed to review the two peers.

---------------------------------------------------------
#### There are a total of 2 tasks for this assignments:
- Simulating SDE
- Downloading and manipulating stock data

#### General comments:
* Login to your GitHub. (If you have forgotten how to do that, please refer to Assignment #1)
* While still stay logged in GitHub, go to [https://github.com/yongkheng/UECM3763_assign2](https://github.com/yongkheng/UECM3763_assign2)
* Click "fork" button at the top right hand corner. Now your GitHub will have a copy of the UECM3763_assign1 repository. Copy the URL.
* Go to the google form [http://goo.gl/forms/vblJl6e391](http://goo.gl/forms/vblJl6e391).
* Fill in your name, ID and the URL to your newly forked repository.
* Answer the question in the google form and submit.
* Clone the repository to your PC.
* In the local repository, there are 4 empty files: gbm.py, mr.py, download_data.py, and report.docx.
* The word file report.dox is an empty file. You will write your report on the findings in Task 1 and Task 2 in this report.docx and upload to your github.



---------------------------------------------------------

## Task 1 -- Simulating SDE

Objectives:
- Simulate geometric Brownian motion and mean reversal process
- Calculate expectations and probability from simulations.


#### 1. Simulating geometric Brownian motion

Consider the following geometric Brownian motion (GBM):

```
dS(t) = 0.1 dt + 0.26 dB(t); S(0) = 39
```

- What is the expectation value of S(3)?
- What is the variance of S(3)?


Edit the file "gbm.py" to simulate 1000 runs of GBM for 0 < t < 3. (Refer to lecture slides.) 

- Plot only **5** realizations of the GBM with proper labels.
- (For the following, please explain how you obtained the values.)
- Calculate the expectation value of S(3) based on the simulation. 
- Calculate the variance of S(3).
- Calculate P[S(3)> 39].
- Calculate E[S(3) | S(3) > 39].


#### 2. Simulating mean reversal process

Consider the following process:

```
dR(t) = [0.064 - R(t)] dt + 0.27 R(t) dB(t); R(0) = 3
```

Edit the file "mr.py" to simulate 1000 runs of above mean reversal process for 0 < t < 1.

- Plot only **5** realizations of the mean reversal process with proper labels.
- (For the following, please explain how you obtained the values.)
- Calculate the expectation value of R(1) based on the simulation. 
- Calculate P[R(1)> 2].


------------------------------------------------------------

## Task 2 -- Downloading and manipulating stock data

Objective:
- to download stock data from Yahoo!Finance
- to perform basic manipulation on stock data

#### 1. FTSE Bursa Malaysia KLCI Index
Investigate the FTSE Bursa Malaysia KLCI Index
- How many components stocks are there?
- create a table list the following information for all the component stocks: Stock Name, Stock Code, Stock Sector, Weightage in FTSEKLCI, PE Ratio, Net Market Capital.

#### 2. Downloading data

Consider the following code is an example that downloads daily data for a counter called Vitrox (code: 0097) from Yahoo!Finance starting from 1 Jan 2010 until 1 May 2015.

```
from pandas.io.data import DataReader as DR
from datetime import datetime as dt

start = dt(2010, 1, 1)
end = dt(2015, 5, 1)
data = DR("0097.KL", 'yahoo', start, end)
```

Complete the following tasks for Task 2:
- Choose 1 FTSEKLCI component of your choice, say counter X.
- Download at least 3 years of daily data for counter X.
- Plot a 5-day moving average plot for the downloaded data. Explain how you calculate the 5-day moving average.
- Download FTSEKLCI daily data for the same duration as your data for X.
- Compute the correlation of your counter X with FTSEKLCI.


-------------------------------------------------------------
One you have submitted your assignment, you may go to [http://goo.gl/forms/AGBsRLCH3L](http://goo.gl/forms/AGBsRLCH3L) to do your peer review starting 27/7/2015 (Monday) after 12:00 noon.
