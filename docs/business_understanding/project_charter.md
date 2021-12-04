# Project Charter

## Business background

* Who is the client, what business domain the client is in.

  We're going to develop this technology for those in the music industry, mainly for inspirational purposes and creation of music lyrics.
  
* What business problems are we trying to address?

  Optimizing the lyrics production for the new artists trying to emerge and grow, also for producers.

## Scope
* What data science solutions are we trying to build?

  Generative Model of text, based on Long short-term memory (LSTM) and Recurrent Neural Networks (RNN).
  
* What will we do?

  Recurrent Neural Networks to generate lyrics given an initial phrase or phrases and fixed lenght. 
  
* How is it going to be consumed by the customer?

  The consumer will have an archive containing the lyrics of the song, ready for production as an output. 
  The client will also have their own database of lyrics for training the model. 
  This database will have the same structure than the original one giving as an input of the tool the list of the artists and the number of songs wanted.

## Personnel
* Who are on this project:
	* JWJ Team:
		* Project lead: Juan Sebastian Lara, Melissa de la Pava
		* PM: William Agudelo
		* Data scientist(s): Juan Carranza, Juan Munoz, Jaime Vera 
		* Account manager: William Agudelo
		* Deployment: Jaime Vera, Juan Carranza
	* Client:
		* Data administrator: Juan Sebastian Lara, Melissa de la Pava
		* Business contact: Juan Sebastian Lara, Melissa de la Pava
	
## Metrics
* What are the qualitative objectives?

  Improve the quality of music production of the artist | producer. 
  
* What is a quantifiable metric?

  Improve the quantity of songs accepted by the record label | Improve the awareness of the music produced and posteriorly increase sales.
  
* Quantify what improvement in the values of the metrics are useful for the customer scenario.

  Increase Lyrics acceptation by at least 15%.
  
* What is the baseline (current) value of the metric?
  
  Usually the lyric acceptation by the record label is around 30 percent.
  
* How will we measure the metric?

  Expected time of record label acceptancy and lyrics correction.

## Plan
* Phases (milestones), timeline, short description of what we'll do in each phase.
1. Creating common server for working
2. Adapt python scripts for data extraction
3. Adapt python scripts for data preprocessing
4. Adapt python scripts for modelling and evaluation
5. Create scripts for giving the output to the client in txt format

Timeline - 3 weeks from now, approximately Dec 16th - 2021

## Architecture
* Data
  * What data do we expect? Raw data in the customer data sources.
	- Plain text files containing the lyrics for training of model or the list of the artist provided by the client
* Data movement from on-prem to Azure using ADF or other data movement tools (Azcopy, EventHub etc.) to move either
  * For every model, we will pick all the available data for constructing the richest possible lyrics database.

* What tools and data storage/analytics resources will be used in the solution.
  * Python for feature construction, aggregation and sampling
  * Git for colaboratory working

* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
  * How will the customer use the model results to make decisions
	- Accepting / Rejecting partial or total the lyrics in the txt files
  * Data movement pipeline in production
	- Along the preprocessing and modelling scripts in a common corpus
  * Make a 1 slide diagram showing the end to end data flow and decision architecture
    * If there is a substantial change in the customer's business workflow, make a before/after diagram showing the data flow.

## Communication
* How will we keep in touch? Weekly meetings?

  We will be in touch weekly.
  
* Who are the contact persons on both sides?
  
  William Agudelo, Juan Sebastian Lara, Melissa de la Pava
