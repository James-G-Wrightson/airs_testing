Image /page/0/Picture/0 description: The image shows the word "energies" in brown, next to a brown square containing a yellow lightning bolt.

*Article*

# **An Experimental Study of the Impact of Dynamic Electricity Pricing on Consumer Behavior: An Analysis for a Remote Island in Japan**

# **Thoa Thi Kim Nguyen <sup>1</sup> , Koji Shimada 2,\*, Yuki Ochi <sup>3</sup> , Takuya Matsumoto <sup>4</sup> , Hiroshi Matsugi <sup>5</sup> and Takao Awata <sup>6</sup>**

- <sup>1</sup> Graduate School of Economics, Ritsumeikan University, 1-1-1 Nojihigashi, Kusatsu, Shiga 525-8577, Japan; chipntkt@gmail.com
- <sup>2</sup> Faculty of Economics, Ritsumeikan University, 1-1-1 Nojihigashi, Kusatsu, Shiga 525-8577, Japan
- <sup>3</sup> E-konzal, 207, 3-8-15, Nishinakajima, Yodogawa, Osaka 532-0001, Japan; ochi.ekonzal@gmail.com
- 4 Information Science and Technology Center, Kobe University, 1-1 Rokkodai-cho, Nada-ku, Kobe 657-8501, Japan; tmat@al.cs.kobe-u.ac.jp
- <sup>5</sup> Hyogo Prefectural Institute of Technology, 3-1-12 Yuihira-cho, Suma-ku, Kobe 654-0037, Japan; h\_matsugi@yahoo.co.jp
- <sup>6</sup> Kei Communication Technology Inc., Shinko Building 8F, 8 Kaigandori, Chuo-ku, Kobe 650-0024, Japan; awata@ieee802.co.jp
- **\*** Correspondence: shimada@ec.ritsumei.ac.jp; Tel.: +81-77-561-5183

Academic Editor: Giovanni Pau

Received: 31 October 2016; Accepted: 12 December 2016; Published: 20 December 2016

**Abstract:** The aim of this research was to investigate how consumer behavior changes after application of dynamic electricity pricing and the persistence of those changes. Based on the investigation results, the authors also discuss the policy implications of demand management to shift consumption to days that have more solar radiation, while at the same time reducing overall consumption. The dynamic pricing experiment was implemented on Nushima Island, located in the center of Japan, with the participation of 50 households. The methodologies used in this study are panel analysis with random effects, and the difference in differences method. Several linear regression analyses are performed to predict hourly electricity usage from a number of explanatory variables, such as life-style factors, the frequency of access to the visualization website, control for weather factors (wind speed and temperatures), and other attributes of the households to predict the log of hourly electric energy consumption. The results show that dynamic pricing brought about 13.8% reduction of electric energy consumption in comparison with the pre-experiment period. Also, by applying a new experimental design approach, this study finds data supportive of habit formation by participants. Based on the findings, this research tries to develop a policy for sustainable energy conservation in remote islands.

**Keywords:** dynamic pricing; electric energy demand response; habit formation

# **1. Introduction**

In Japan, since the earthquake and tsunami on 11 March 2011 precipitated a disastrous accident at the Fukushima Daiichi Nuclear Power Station, much attention has been given to the promotion of renewable energy as an important component of Japan's future energy mix. While it is practical to address the problem created by the shutdown of nuclear power plants by maximizing the usage of existing thermal power plants, it is not possible to immediately increase the supply of electricity. In addition, increased emissions of greenhouse gases, especially CO2, are also a major issue. Even though renewable energies show potential in reducing CO<sup>2</sup> emissions, they have a very low capacity value, which leads to supply uncertainty. Therefore, this study shifts the focus

Image /page/0/Picture/19 description: The image shows the logo for MDPI, a publisher of open access scientific journals. The logo consists of the letters "MDPI" in a bold, sans-serif font, enclosed within a stylized chemical structure, resembling a benzene ring. The letters and the chemical structure are in a dark blue color.

to the perspective of electric energy demand management. To be specific, lowering electric energy consumption can help not only by reducing the costs of serving energy but also by balancing and making the supply-demand system more efficient. Consumers are expected to decrease their electric energy consumption by receiving incentives through dynamic pricing and real-time information via smart meters. value, which leads to supply uncertainty. Therefore, this study shifts the focus to the perspective of electric energy demand management. To be specific, lowering electric energy consumption can help not only by reducing the costs of serving energy but also by balancing and making the supplydemand system more efficient. Consumers are expected to decrease their electric energy consumption

Why was Nushima Island chosen to be the experimental target? Nushima Island is a remote island located in the south of Hyogo prefecture, where electric energy needs rely on supply provided by the Kansai electric power company (Osaka, Japan) (Figure [1\)](#page-1-0) [\[1\]](#page-20-0). The island had an estimated population of about 527 people (statistics as of 2012, Hyogo Prefecture (Hyogo, Japan) [\[2\]](#page-21-0)). At present, the small island confronts a situation in which the Japanese government introduced electric power market liberalization to the general household-level in April 2016 (Agency for Natural Resources and Energy (Tokyo, Japan) [\[3\]](#page-21-1)). Although the new market system can create great advantages for consumers, such as by lowering the prices by empowering them to choose their electric power supplier, it may cause supply volatility by dissolving the market-stabilizing responsibilities that used to be taken on by the regional electric power monopoly suppliers. Consequently, the communities that are not only far away from the mainland, but also difficult to deliver electric energy to, like Nushima, may no longer be a target of electric power companies. In Japan, more than 6500 islands that have the same characteristics of Nushima will be confronted with electric energy shortage issues. by receiving incentives through dynamic pricing and real-time information via smart meters. Why was Nushima Island chosen to be the experimental target? Nushima Island is a remote island located in the south of Hyogo prefecture, where electric energy needs rely on supply provided by the Kansai electric power company (Osaka, Japan) (Figure 1) [1]. The island had an estimated population of about 527 people (statistics as of 2012, Hyogo Prefecture (Hyogo, Japan) [2]). At present, the small island confronts a situation in which the Japanese government introduced electric power market liberalization to the general household-level in April 2016 (Agency for Natural Resources and Energy (Tokyo, Japan) [3]). Although the new market system can create great advantages for consumers, such as by lowering the prices by empowering them to choose their electric power supplier, it may cause supply volatility by dissolving the market-stabilizing responsibilities that used to be taken on by the regional electric power monopoly suppliers. Consequently, the communities that are not only far away from the mainland, but also difficult to deliver electric energy to, like Nushima, may no longer be a target of electric power companies. In Japan, more than 6500 islands that have the same characteristics of Nushima will be confronted with electric energy shortage issues.

<span id="page-1-0"></span>Image /page/1/Figure/3 description: This image shows a map of Japan. The map includes the islands of Hokkaido, Honshu, Shikoku, and Kyushu. The cities of Tokyo, Osaka, and Kobe are labeled on the map. The island of Awajishima is also labeled, as is the island of Nushima.

**Figure 1.** The location of Nushima Island. Source: Web-Japan.org [1]. **Figure 1.** The location of Nushima Island. Source: Web-Japan.org [\[1\]](#page-20-0).

community's self-control of its electric energy demand through dynamic pricing. According to the results of this experiment, this paper may establish a smart-energy community's model that is both environmentally friendly and resistant to the electric power market's instability. The term "dynamic pricing" used in this research is basically a concept that extended from the The aim of the dynamic pricing experiment in Nushima is to assess the possibility of the community's self-control of its electric energy demand through dynamic pricing. According to the results of this experiment, this paper may establish a smart-energy community's model that is both environmentally friendly and resistant to the electric power market's instability.

concept of time-of-use (TOU) rates. TOU is an advanced extension of a multiple tariff, which includes a critical peak price as well as a peak and off-peak price. The idea of these prices is to shift consumption to off peak when the cost of generating and procuring electric energy is lower than in peak period. Additionally, extreme weather conditions may also require a critical peak price, which would reflect the cost of procuring energy when demand is highest. This kind of extreme weather we might encounter in summer at the height of holidays, or in the most frozen days of winter. For another The term "dynamic pricing" used in this research is basically a concept that extended from the concept of time-of-use (TOU) rates. TOU is an advanced extension of a multiple tariff, which includes a critical peak price as well as a peak and off-peak price. The idea of these prices is to shift consumption to off peak when the cost of generating and procuring electric energy is lower than in peak period. Additionally, extreme weather conditions may also require a critical peak price, which would reflect the cost of procuring energy when demand is highest. This kind of extreme weather we might encounter

in summer at the height of holidays, or in the most frozen days of winter. For another example of TOU rate, an electric power supplier may offer a tariff that differentiates between several time periods throughout the weekday or weekends [\[4\]](#page-21-2). In this research, dynamic pricing interventions are prompted based on weather forecasts.

The effects of dynamic pricing in electric energy demand response have been researched mainly in developed countries such as the United States, Canada, Japan, etc. Especially since the energy crisis of 2000–2001 in the western United States, dynamic pricing's impact on electric energy consumption constraint has been receiving more attention. Faruqui and Sergici [\[5\]](#page-21-3) summarized in total 15 experimental studies related to dynamic pricing programs in the past. Many of those experiments were conducted in the United States. Almost all of those experimental studies are not fully based on Randomized Controlled Trials (RCT), and use TOU rates and critical peak pricing (CPP) tariffs to stimulate consumers to lower their usage. According to Faruqui and Sergici [\[5\]](#page-21-3), TOU rates and CPP tariffs were reported to bring about a drop in peak demand from 3% to 6% and from 13% to 20%, respectively. Most of the preceding studies applied panel data to analyze results, and the effects of dynamic pricing were observed by the difference-in-differences (DID) estimator, utilizing the treatment group with the dynamic pricing rate, and the control group with existing rates. Even when applying the DID estimator, unless the participants are divided into two groups at random to receive interventions, the experiment has a quasi-experimental design where "the cause is manipulable and occurs before the effect is measured" (Shadish et al. [\[6\]](#page-21-4), p. 14). Regarding dynamic pricing rates, the previous studies tended to adopt multiple price points, which allow predicting not only the impact of one given rate in the study but also other rates, rather than a single time-varying rate.

The recent field experiment of Wolak [\[7\]](#page-21-5) is one of the RCT experimental studies which have a strong impact. According to his finding, while CPP tariffs were reported to bring about a 13% reduction of electric energy consumed at peak period, critical peak rebate (CPR) tariffs reduced the consumption by only 5.3%.

Nonetheless, a big question of whether energy-saving effects persist or not still remains. According to Frey and Rogers [\[8\]](#page-21-6), persistence is caused by forming psychological habits, changing the way people think, changing future costs, and utilizing external reinforcement. With regard to this issue, starting with the Home Energy Reports (HERs) of the Sacramento Municipal Utility District Electricity Company (SMUD, Sacramento, CA, USA), there have been dozens of experiments conducted. Summarizing the transition of HERs, Khawaja and Stewart [\[9\]](#page-21-7) found that if it is assumed that the load curtailing effect of the last year of a three-year experiment was 100%, the effect of the first year was 57%, and that of the second was 87%.

Allcott and Rogers [\[10\]](#page-21-8) analyzed the persistence of HERs' effect in detail, based on the data of three demand response programs. All these programs had a population comprising approximately 70,000–80,000 households, who were comparatively heavy energy users. The population was randomly appointed to treatment and control groups. The treatment group was also randomly assigned to several groups which received reports with difference frequencies. The estimation results disclosed that for the group which stopped receiving reports after two years of the experiment, the effect was gradually diminishing. However, the effect still retained its persistence during the 2 years following the withdrawal.

Apparently, the ideal approach to verify the persistence of a demand response program is to lengthen experimental periods, yet due to limits of budget and difficulties in acquiring approvals of projects, it is arduous work to keep an experiment running for a long time. To tackle this issue, this study makes a new approach, which is explained at the end of this section.

In Japan, demand response programs are still in their foundation stage. There are several experimental studies on electric demand response and dynamic pricing that have been carried out lately, such as in Kyoto, Yokohama, Toyota, and Kitakyushu, the four major smart-community projects currently being sponsored by the government. The impact of dynamic pricing is tested through smart meters and visualization systems. In some projects, the visualization websites are connected through tablets provided to participants in order to receive notification of critical peaks. These systems give the participating households an opportunity to confirm their point balances. The participants are given a certain amount of points, which are then subtracted according to their peak hour demand. They are then paid an incentive payment based on the remaining point balance after the experiment period. One of the most considerable experiments is the smart city operational experiment in Keihanna city (Kyoto) during 2012–2013. In the experiment, a combination of TOU rates and CPP was used in both the summer and winter. That study demonstrated that in comparison with summer, the winter consumption reduction through TOU improved from 8.2% to 14.9%, but diminished from 14.1% to 6.4% through CPP (Japan Smart City Report [\[11\]](#page-21-9)).

On the other hand, there is another experimental study conducted in Keihanna city by Ito et al. [\[12\]](#page-21-10). In the study, they focused on the comparison between CPP tariffs and non-monetary "nudges" (or moral suasion). The result suggested that while CPP tariffs had a treatment effect of approximately 16%, non-monetary incentives only helped reduce consumption by 3%. The authors assessed the durability of moral suasion and economic incentives by comparing the effects of repeated interventions. Moreover, to investigate the persistence of the experiment, they compared the consumption of treatment and control groups during post-experimental period. However, there is a limitation in their estimation. Although they applied an excellent design of a random controlled trial, their regression model did not appear to have sufficient components of the difference in differences method. Their main empirical equation is the following:

$$
\text{Ln } x_{it} = \alpha M_{it} + \beta E_{it} + \theta_i + \lambda_t + \mu_{it}
$$

In this equation, *M*it equals 1 if the household is in the moral suasion group and receives the treatment; *E*it equals 1 if the household is in the economic incentive group and receives the treatment. In other words, these two variables are the interaction terms of the treatment group and experimental period dummies, which should have also been included in the regression model.

There is also a study by Shimada et al. [\[13\]](#page-21-11) that evaluated the impacts of real-time feedback ("nudges") and dynamic pricing on management by using the daily electric energy consumption data in Nushima. In this study, the authors used a quasi-experimental research method, which used preand post-test design. They compared the difference between the before and after experiment periods to evaluate the effects of dynamic pricing. They found that real-time feedback and dynamic pricing were effective in controlling electric energy demand. Specifically, when the frequency of access to tablet PCs reached three times per day, the estimated reductions of feedback and dynamic pricing were 20% and 2% respectively. However, a query on the method of calculating dynamic pricing effects can be raised, since those effects were estimated as the difference between the reduction rates of the period applying feedback—pricing and of the period which applied only feedback. Precisely, these two periods' characteristics are different from each other (much like spring and summer electric energy consumption behaviors are absolutely dissimilar). In addition, according to Torgerson and Torgerson [\[14\]](#page-21-12), pre- and post-test studies have some limitations, since they will over-estimate any benefit of a policy because of "regression to the mean effects" and "temporal changes".

This study is an analysis which extends the study of Shimada et al. [\[13\]](#page-21-11) to investigate the impacts of dynamic pricing more accurately, through adopting a control group and a treatment group. Although this study inherits the originality of establishing tariffs based on the weather (sunny, cloudy, rainy), which is supposed to dominate the solar photovoltaic generation system, it focuses on the effects of pricing based on the premise that visualization's effects were already excluded. Therefore, this study picks up the short periods when the subtraction rates are applied to compare with the same-length-period right before and after them, and conduct analysis based on hourly data.

The participants were divided into control and treatment groups by random selection. Nevertheless, unlike previous studies, this study attempts a new approach to examine the persistence or habit formation in post-experimental period by making an inverse change between the two groups in the winter's experiment.

This study also adds hourly effects as life-style factors on demand constraint. Moreover, during the experiment the fact that there are households who do not pay attention to the pricing system at all was noticed, and thus the study also assesses the frequency of access's marginal effect, which has not been done in previous studies. The following hypothesis can be raised: both frequency of access and dynamic pricing have negative impacts on electric energy consumption, and these impacts are persistent over long periods of time.

## **2. Experimental Design and Regression Models**

### *2.1. Experimental Design*

#### 2.1.1. Design

The analysis was conducted with data from the field experiment on Nushima Island with the following two objectives:

(1) To estimate the effects of dynamic pricing and its persistence on electric energy consumption.

In other words, it may be expected that the treatment group acquires a habit formation that persists even after withdrawing the experiment. If habit formation is observed, it will be a clue for policy implications that fulfill the second objective of this research as follows.

(2) To amplify an appropriate pricing method according to the daily fluctuations of solar electricity generation on the island.

The experiment that has been carried out in Nushima since 2012 is a three-year project. To invite as many participating households as possible, the experiment was designed with initial benefits from the beginning, such as free installation of smart meters and tablet personal computers. Thanks to the cooperation of the branch office of Minamiawaji City in Nushima Island, 50 households were randomly assigned (ten households in each district, Kita District, Naka District, Minami District and Tomari District). A guidance session has been held with the attendance of all 50 households to explain the experiment and to start installing the equipment. All 50 households confirmed their participation. Although there is a limitation of sample size, this experiment is a randomized controlled trial, since its set-up process is similar to previous field experiments on electric energy demand response by Faruqui and Sergici [\[15\]](#page-21-13) or Jessoe and Rapson [\[16\]](#page-21-14) (in the middle of the study, one household in the treatment group withdrew from the experiment).

In 2012, smart meters (see Figure [2\)](#page-5-0) were installed in the participants' houses. In May 2013, tablet PCs (see Figure [3\)](#page-5-1), which provide access to feedback on electric energy consumption, were distributed to the participants. Finally, dynamic pricing was introduced in the summer (August and September) of 2015 and the winter (January and February) of 2016.

The control group is the group of 25 households that received a smart meter, a tablet PC, and a reward of 5000 Japanese Yen in summer at the end of the experiment. Besides these, this group did not receive any other special treatment or incentives. The study group is another 25 households that received a smart meter, a tablet PC, and a monetary incentive for energy conservation, as well as a reward of 5000 Japanese Yen. The monetary incentive will be explained in detail in the next section.

Additionally, to investigate the habit formation process of the treatment group, an inverse change was conducted between the two groups in the winter experiment. That means the control group became treatment group in the winter and received a monetary incentive through their demand constraint. Therefore, if habit formation happens, there should be no significant differences between the two groups, in terms of a treatment effect appearing during the experimental period in the winter.

<span id="page-5-0"></span>Image /page/5/Picture/1 description: The image shows a smart meter and an electrical box mounted on a wall. The smart meter is a rectangular device with a digital display. The electrical box is a square box with a hinged lid. The smart meter is connected to the electrical box by a cable. The electrical box is circled in yellow.

**Figure 2.** A smart meter established at one household. **Figure 2.** A smart meter established at one household.

<span id="page-5-1"></span>Image /page/5/Figure/3 description: The image shows a tablet PC displaying information feedback on electric power consumption. The screen is divided into sections. The first section, titled "Electric power consumptions in your home," presents data in a table format with columns for "Now (W)," "Today (Wh)," "Yesterday (Wh)," and "This month (Wh)." The corresponding values are 450, 3,000, 7,500, and 27,000, respectively. The second section, "Per-capita electric power consumption," also uses a table format with columns for "Now (W/person)," "Today (Wh/person)," "Yesterday (Wh/person)," and "This month (Wh/person)." It compares "Your house" with "Average of all houses." For "Your house," the values are 150, 1,000, 2,500, and 9,000. For "Average of all houses," only "Yesterday" and "This month" are provided, with values of 3,625 and 10,756, respectively. Below the table is a bar graph showing "Per-capita consumption (Wh/person)" over "Time." The final section, "Lowest electric power consumption ranking," indicates "Your rank: 14th (yesterday)." The image is labeled as "Figure 3. Information feedback on tablet PC. Source: Shimada et al. (2015) [13]."

**Figure 3.** Information feedback on tablet PC. Source: Shimada et al. (2015) [\[13\]](#page-21-11).

reward of 5000 Japanese Yen in summer at the end of the experiment. Besides these, this group did not receive any other special treatment or incentives. The study group is another 25 households that received a smart meter, a tablet PC, and a monetary incentive for energy conservation, as well as a reward of 5000 Japanese Yen. The monetary incentive will be explained in detail in the next section. Additionally, to investigate the habit formation process of the treatment group, an inverse This study collected hourly data of household electric energy consumption. The installed digital smart meters allow collecting household energy consumption at one second intervals. Based on the collected one-second-interval data, the authors calculated hourly data from the summer of 2015 to the winter of 2016. In addition to the usage data, demographic data was collected through a pre-experimental questionnaire survey.

change was conducted between the two groups in the winter experiment. That means the control group be[cam](#page-6-0)e treatment group in the winter and received a monetary incentive through their demand constraint. Therefore, if habit formation happens, there should be no significant differences between the two groups, in terms of a treatment effect appearing during the experimental period in the winter. This study collected hourly data of household electric energy consumption. The installed digital smart meters allow collecting household energy consumption at one second intervals. Based on the To summarize, a description of all variables used in this research is provided in the Nomenclature part. Table 1 presents the descriptive statistics of demographic variables and pre-experimental data of electric energy usage and access frequency by group. A comparison between the two groups demonstrates a statistical balance in the observations. This fact is also indicated in Table [2,](#page-6-1) which shows estimated differences between the two groups and the *p*-values of testing the hypothesis that the differences (C-T) are not equal to zero.

<span id="page-6-0"></span>

| Variables                          | Control Group (C) |       |                    |     | Treatment Group (T) |              |       |                    |     |      |
|------------------------------------|-------------------|-------|--------------------|-----|---------------------|--------------|-------|--------------------|-----|------|
|                                    | Observations      | Mean  | Standard Deviation | Min | Max                 | Observations | Mean  | Standard Deviation | Min | Max  |
| Hourly electric energy consumption | 18,526            | 601.6 | 618.8              | 100 | 4600                | 19,934       | 551.2 | 408.99             | 100 | 3900 |
| PlFrequency of access              | 18,556            | 0.005 | 0.115              | 0   | 6                   | 20,000       | 0.007 | 0.106              | 0   | 6    |
| Household member                   | 25                | 2.760 | 1.090              | 1   | 5                   | 24           | 2.750 | 1.150              | 1   | 5    |
| Happye contractor                  | 25                | 0.280 | 0.458              | 0   | 1                   | 25           | 0.400 | 0.500              | 0   | 1    |
| Air-conditioner                    | 24                | 2.458 | 0.658              | 1   | 3                   | 25           | 2.480 | 0.653              | 1   | 3    |
| Fridge                             | 24                | 1.250 | 0.531              | 1   | 3                   | 23           | 1.435 | 0.590              | 1   | 3    |
| Commercial Fridge                  | 24                | 0.500 | 0.884              | 0   | 3                   | 25           | 0.280 | 0.458              | 0   | 1    |
| Wooden house                       | 22                | 0.818 | 0.394              | 0   | 1                   | 25           | 0.800 | 0.408              | 0   | 1    |

Table [2](#page-6-1) presents means and the standard errors (in brackets) of the differences. The differences of the two major variables, hourly electric energy consumption and frequency of access, are small, and the hypothesis that they exist is rejected with statistical significance.

The numbers of "happye" contractors, air conditioners, fridges, commercial fridges, and wooden houses show statistically significant differences at the 0.05 level, but they are not important variables in the estimate of this study. Consequently, the results in Table [2](#page-6-1) suggest that these two samples are statistically similar in terms of the key observable variables of interest.

<span id="page-6-1"></span>

|                                    |               | <i>p</i> -Value |             |             |
|------------------------------------|---------------|-----------------|-------------|-------------|
| Variables                          | C-T           | H: Diff < 0     | H: Diff ≠ 0 | H: Diff > 0 |
| Hourly electric energy consumption | 50.34 (5.31)  | 1.00            | 0.00        | 0.00        |
| Household member                   | 0.010 (0.32)  | 0.50            | 0.96        | 0.49        |
| Frequency of access                | -0.002 (0.00) | 0.04            | 0.07        | 0.96        |
| Happye contractor                  | -0.120 (0.14) | 0.19            | 0.38        | 0.81        |
| Air-conditioner                    | -0.021 (0.19) | 0.45            | 0.91        | 0.54        |
| Fridge                             | -0.184 (0.16) | 0.13            | 0.26        | 0.86        |
| Commercial Fridge                  | 0.220 (0.20)  | 0.86            | 0.27        | 0.14        |
| Wooden house                       | 0.018 (0.12)  | 0.56            | 0.88        | 0.44        |

**Table 2.** Differences between the two groups. Standard errors in brackets.

#### 2.1.2. Dynamic Pricing Treatment

The dynamic pricing experiments were carried out from 1 September to 14 September 2015 and from 19 January to 1 February 2016. At the beginning of the experiment, each participating household was allocated 7000 points and points were then subtracted according to their electric energy consumption. The participants could exchange their remaining balance of points into cash at the end of the experiment (one point equals one Japanese Yen).

There are three types of designed subtraction rates and the rate changed daily based on the weather forecast. The rates were set up so that the deduction rate on cloudy or rainy days was higher than on sunny days since it is assumed that participants live in a smart-energy community where electric energy is supplied by renewable power (such as solar power and energy stored in batteries). Since the solar electricity generation system would produce less energy on cloudy or rainy days, energy stored in the batteries would decrease.

The rate is 20 points per (kWh/person) when the weather forecasts of both the preceding and following days are sunny, 30 points when the forecast of either the preceding or following days is sunny, and 40 points when the forecast of neither the preceding day nor the following day is sunny.

<span id="page-7-0"></span>Table [3](#page-7-0) shows the daily weather forecast and the deduction rates during the period of the dynamic pricing experiment in summer, and Table [4](#page-7-1) shows those in the winter experiment.

| Date              | Weather Forecast | Subtraction Rate (Points/(kWh/Person)) |
|-------------------|------------------|----------------------------------------|
| 1 September 2015  | Rainy            | 40                                     |
| 2 September 2015  | Rainy            | 40                                     |
| 3 September 2015  | Rainy            | 40                                     |
| 4 September 2015  | Sunny            | 30                                     |
| 5 September 2015  | Sunny            | 20                                     |
| 6 September 2015  | Cloudy           | 30                                     |
| 7 September 2015  | Rainy            | 40                                     |
| 8 September 2015  | Rainy            | 40                                     |
| 9 September 2015  | Rainy            | 40                                     |
| 10 September 2015 | Rainy            | 40                                     |
| 11 September 2015 | Rainy            | 30                                     |
| 12 September 2015 | Rainy            | 20                                     |
| 13 September 2015 | Cloudy           | 20                                     |
| 14 September 2015 | Cloudy           | 20                                     |

**Table 3.** Daily weather forecast in summer.

**Table 4.** Daily weather forecast in winter.

<span id="page-7-1"></span>

| Date            | Weather Forecast | Subtraction Rate (Points/(kWh/Person)) |
|-----------------|------------------|----------------------------------------|
| 19 January 2016 | Snowy            | 30                                     |
| 20 January 2016 | Snowy            | 40                                     |
| 21 January 2016 | Rainy            | 30                                     |
| 22 January 2016 | Sunny            | 20                                     |
| 23 January 2016 | Sunny            | 20                                     |
| 24 January 2016 | Cloudy           | 30                                     |
| 25 January 2016 | Snowy            | 40                                     |
| 26 January 2016 | Sunny            | 30                                     |
| 27 January 2016 | Sunny            | 20                                     |
| 28 January 2016 | Sunny            | 20                                     |
| 29 January 2016 | Rainy            | 30                                     |
| 30 January 2016 | Rainy            | 40                                     |
| 31 January 2016 | Sunny            | 30                                     |
| 1 February 2016 | Sunny            | 20                                     |

#### *2.2. Hypotheses*

This study tests two main hypotheses. The first hypothesis is based on a conventional economic theory, the price elasticity of demand, which predicts that the monetary incentive group, the treatment group, reduces their consumption according to the price fluctuation. A comparison of consumption across the control and treatment groups was conducted to test the hypothesis.

The second hypothesis relates to potential habit formation that can be stimulated by repeated interventions (Becker and Murphy [\[17\]](#page-21-15)). To test this hypothesis, even after withdrawing the treatments of summer and winter, electric energy consumption data continued to be collected. The author tested whether the monetary incentive effect disappeared after withdrawing the treatments. In addition, in the second round of the experiment, the winter trial, there was an inverse change so that the summer control group became the winter treatment group, and the summer treatment group became the winter

### *2.3. Methodologies and Empirical Models*

This study employs panel data analysis to assess treatment effects of dynamic pricing. Since energy demand varies according to various factors, such as ambient temperature, household size, and numbers of household electrical appliances etc., the effects of dynamic pricing should be estimated separately from other factors that may influence electric energy usage. Since this study takes a large number of explanatory variables into consideration and these control factors are time-invariant, regression models are run with random effects. To assess treatment effects, the difference in differences method was employed. *Energies* **2016**, *9*, 1093 9 of 21 and numbers of household electrical appliances etc., the effects of dynamic pricing should be estimated separately from other factors that may influence electric energy usage. Since this study takes a large number of explanatory variables into consideration and these control factors are timeinvariant, regression models are run with random effects. To assess treatment effects, the difference

The number of total samples excluding missing values amounts to 18,187 in the summer and 32,893 in the winter, which were collected from the 50 households over the two periods of 34 days from 28 August 2015 to 30 September 2015, and 46 days from 1 January 2016 to 15 February 2016. in differences method was employed. The number of total samples excluding missing values amounts to 18,187 in the summer and 32,893 in the winter, which were collected from the 50 households over the two periods of 34 days

Two main regression models were conducted; the first model is to assess the effects of monetary-incentive-based dynamic pricing. The second model is to investigate habit formation after the experiment. This study also includes the variables of weather factors, hourly effects and other attributes of the participants. These two main models are used for both summer's and winter's trials. from 28 August 2015 to 30 September 2015, and 46 days from 1 January 2016 to 15 February 2016. Two main regression models were conducted; the first model is to assess the effects of monetaryincentive-based dynamic pricing. The second model is to investigate habit formation after the experiment. This study also includes the variables of weather factors, hourly effects and other

### 2.3.1. First Model: Effect of Monetary-Incentive-Based Dynamic Pricing

Applying the basic model of the DID method to assess the effects of dynamic pricing, this study investigates the difference between the control group and treatment group in pre-experimental period and experimental period by the following regression model: 2.3.1. First Model: Effect of Monetary-Incentive-Based Dynamic Pricing Applying the basic model of the DID method to assess the effects of dynamic pricing, this study investigates the difference between the control group and treatment group in pre-experimental

$$
Log(Y_{it}) = \alpha + \beta_1 U_{it} + \beta_2 T_{it} + \beta_3 U_{it} \cdot T_{it} + \beta_4 C_{it} + \mu_{it} + \varepsilon_{it}
$$
(1)

In this equation, Log (*Y*it) denotes the natural log of hourly electric energy consumption (Wh) as the dependent variable. *U*it, *T*it, and *U*it·*T*it are component parts of the variable set of DID method. *U*it presents treatment group's dummy variable, in which the treatment group is coded 1 and the control group is coded 0. Tit is a dummy variable that takes the value 1 in the treatment period (from 1 September to 14 September in the summer (Figure 4)). *U*it·*T*it is the interaction term of the two dummy variables above and β<sup>3</sup> presents the coefficient the experiment's effect. Besides, µit is the unobserved effect, which is uncorrelated with all the independent variables in the model. In this equation, Log (*Y*it) denotes the natural log of hourly electric energy consumption (Wh) as the dependent variable. *U*it, *T*it, and *U*it∙*T*it are component parts of the variable set of DID method. *U*it presents treatment group's dummy variable, in which the treatment group is coded 1 and the control group is coded 0. Tit is a dummy variable that takes the value 1 in the treatment period (from 1 September to 14 September in the summer (Figure 4)). *U*it∙*T*it [is](#page-8-0) the interaction term of the two dummy variables above and β3 presents the coefficient the experiment's effect. Besides, μit is the unobserved effect, which is uncorrelated with all the independent variables in the model.

<span id="page-8-0"></span>Image /page/8/Figure/10 description: The image shows a timeline of an experiment with three periods: Pre-Experimental Period, Experimental Period, and Post-Experimental Period. The Pre-Experimental Period starts on Aug 28 and ends on Sep 1. The Experimental Period starts on Sep 1 and ends on Sep 14. The Post-Experimental Period starts on Sep 14 and ends on Sep 30. The Pre-Experimental Period is labeled as t-1, the Experimental Period is labeled as t, and the Post-Experimental Period is labeled as t+1.

**Figure 4.** Summer time chart. **Figure 4.** Summer time chart.

Beside the three main variables of DID, there is also a set of other control variables which is presented as *C*it in Equation (1). The control variables are frequency of accesses to the visualization system, variables of weather condition (such as temperatures, wind speed), hourly effects such as the life-style factors, and households' attributes (those factors refer to the households' characteristics that Beside the three main variables of DID, there is also a set of other control variables which is presented as *C*it in Equation (1). The control variables are frequency of accesses to the visualization system, variables of weather condition (such as temperatures, wind speed), hourly effects such as the

life-style factors, and households' attributes (those factors refer to the households' characteristics that dominate energy consumption, such as the numbers of household members, refrigerators, commercial freezers, and air conditioners, as well as regional dummy variables. The dummy variables "happye contractor" expresses whether all energy in a household was electric energy or if non-electrical heating appliances were used. The dummy variable "wooden house" explains whether the household was living in a timber house or not).

The weather conditions are presented by variables such as cooling degrees, heating degrees, and hourly average wind speed. The cooling and heating degrees refer to how many degrees the ambient temperature is higher or lower than given base temperatures. The base temperatures are assumed to be equal to the temperatures at which humans feel comfortable. The base temperatures for cooling degrees and heating degrees were set at 24 ◦C and 18 ◦C respectively. For the winter period, similar regression models are estimated as well, but without cooling degrees in control variables. For the summer period, due to the weather conditions, both cooling degrees and heating degrees variables are included in the model. However, in the winter regression, cooling degrees variable is excluded. *Energies* **2016**, *9*, 1093 10 of 21

The life-style factors, which demonstrate the general trends in the impacts of dynamic pricing on energy consumption's changes by time, are denoted by the interaction variables of hourly dummy variables and treatment effect dummy variables. The life-style factors, which demonstrate the general trends in the impacts of dynamic pricing on energy consumption's changes by time, are denoted by the interaction variables of hourly dummy variables and treatment effect dummy variables.

#### 2.3.2. Second Model: Habit Formation

To detect whether habit formation occurs after withdrawing the experiment, basically the same regression model as model (1) is used, but the main DID variables are slightly changed. The regression model for habit formation in summer is presented as follows: 2.3.2. Second Model: Habit Formation To detect whether habit formation occurs after withdrawing the experiment, basically the same regression model as model (1) is used, but the main DID variables are slightly changed. The

$$
Log(Yit) = \alpha + \beta_1 Uit + \beta_2 T'it + \beta_3 U'it + T'it + \beta_4 Cit + \muit + \varepsilonit
$$
 (2)

In order to investigate whether there is habit formation or not, this study takes the difference of the pre-experimental period and post-experimental period. Therefore, the function form of this estimate is kept the same as the regression model (1), but it includes one new variable as *T* 0 it. *T* 0 it is a dummy variable that takes the value of 1 if the treatment group is in the post-experimental period (from 15 September to 30 September in the summer (Figure 5)). In order to investigate whether there is habit formation or not, this study takes the difference of the pre-experimental period and post-experimental period. Therefore, the function form of this estimate is kept the same as the regression model (1), but it includes one new variable as *T*′it. *T*′it is a dummy variable that takes the value of 1 if the treatment group is in the post-experimental period (from 15 September to 30 September in the summer (Figure [5](#page-9-0))).

<span id="page-9-0"></span>Image /page/9/Figure/9 description: The image shows a timeline of an experiment. The timeline is divided into three periods: Pre-Experimental Period, Experimental Period, and Post-Experimental Period. The Pre-Experimental Period starts on Jan 1 and ends on Jan 19. The Experimental Period starts on Jan 19 and ends on Feb 1. The Post-Experimental Period starts on Feb 1 and ends on Feb 15.

**Figure 5.** Winter time chart. **Figure 5.** Winter time chart.

In addition, this study also detects habit formation by setting up an inverse change between the control and treatment groups in the winter. Specifically, if habit formation occurs and the habits persist throughout the winter experiment as well, the two groups are expected to have no differences between each other's electric energy consumption. Therefore, the regression model for the winter is as the following equation: In addition, this study also detects habit formation by setting up an inverse change between the control and treatment groups in the winter. Specifically, if habit formation occurs and the habits persist throughout the winter experiment as well, the two groups are expected to have no differences between each other's electric energy consumption. Therefore, the regression model for the winter is as the following equation:

$$
Log(Y_{it}) = \alpha + \beta_1 U'_{it} + \beta_2 T_{it} + \beta_3 U'_{it} \cdot T_{it} + \beta_4 W_{it} + \mu_{it} + \varepsilon_{it}
$$
\n(3)

is coded 0 and the former control group is coded 1. Tit is a dummy variable that takes the value of 1 if the treatment group is in the treatment period (from 19 January to 1 February in the winter). Wit denotes other control variables excluding cooling degrees. Also, if the habits persist in the long-run, the DID comparing pre-experimental and post-*U*0 it presents an inverse treatment group's dummy variable, in which the former treatment group is coded 0 and the former control group is coded 1. Tit is a dummy variable that takes the value of 1 if the treatment group is in the treatment period (from 19 January to 1 February in the winter). Wit denotes other control variables excluding cooling degrees.

Also, if the habits persist in the long-run, the DID comparing pre-experimental and post-experimental periods in the winter is expected to have no statistically significant result either. We have the regression model as below:

$$
Log (Y_{it}) = \alpha + \beta_1 U'_{it} + \beta_2 T'_{it} + \beta_3 U'_{it} \cdot T'_{it} + \beta_4 W_{it} + \mu_{it} + \varepsilon_{it}
$$
(4)

#### 2.3.3. Price Elasticity of Demand

Even though DID regression may show that the dynamic pricing treatment had a demand-constrained effect, whether households reacted to the marginal change of the deduction rate, or they responded to the overall monetary incentive, at the end of the experiment as a whole the demand-constrained effect is still unexplained. Since these two dissimilar interpretations lead us to two different ways of policy, this study also investigates the hypothesis on price elasticity of demand. Since the deduction rates were established in accordance with the daily weather forecast, regressions are run with daily electric energy consumption. The regression models are determined as the following equations:

$$
Log(YitD) = \alpha + \beta_1 Uit \cdot Xit + \beta_2 Cit + \muit + \varepsilonit
$$
 (5)

$$
Log(Y_{it}^D) = \alpha + \beta_1 U_{it} \cdot Z_{it} + \beta_2 C_{it} + \mu_{it} + \varepsilon_{it}
$$
\n
$$
\tag{6}
$$

$$
Log(Y_{it}^D) = \alpha + \beta_1 U_{it} \cdot W_{it} + \beta_2 C_{it} + \mu_{it} + \varepsilon_{it}
$$
\n<sup>(7)</sup>

In these equations, the outcome variable is daily electric energy consumption, which is presented as *Y*it <sup>D</sup>. *X*it denotes the dummy variable that takes the value of 1 on 20-point-deduction days, value 0 on pre-experimental days. *Z*it presents the dummy variable that takes the value of 1 on 30-point-deduction days, value 0 on pre-experimental days. Wit presents the dummy variable that takes the value of 1 on 40-point-deduction days, value 0 on pre-experimental days. The interaction variables *U*it·*X*it, *U*it·*Z*it, and *U*it·*W*it denote the effects of 20, 30, and 40 point deduction respectively. By comparing their three coefficients, how consumers react to the marginal change of deduction rates can be observed. If the price elasticity of demand works, β<sup>1</sup> (5) , β<sup>1</sup> (6), and β<sup>1</sup> (7) should be smaller than zero, β<sup>1</sup> (5) should be larger than β<sup>1</sup> (6), and β<sup>1</sup> (6) should be larger than β<sup>1</sup> (7). (0 < β<sup>1</sup> (7) < β<sup>1</sup> (6) < β<sup>1</sup> (5)) (β<sup>1</sup> (5) , β<sup>1</sup> (6), and β<sup>1</sup> (7) is β<sup>1</sup> of model (5), (6), and (7)).

## **3. Empirical Results and Discussion**

Since all of the regression models determined in previous sections are estimated with random effect and robust standard errors, there is no problem of heteroscedasticity. Since our panel data is not a balanced one, to detect the unit-roots (stationarity) of variables in the whole sample, a Fisher-type unit-root test is conducted. The Fisher-type unit-root test is a type of ADF test, but is possible for unbalanced data, and the individual series can have time gaps (Kunst [\[18\]](#page-21-16)). The result reveals that the variables used in our models are stationary.

### *3.1. Effects of Monetary-Incentive-Based Dynamic Pricing*

Results for main variables of interest in the summer experiment are presented in Table [5.](#page-11-0) The left-hand column of Table [5](#page-11-0) demonstrates the regression result of model (1), in which the coefficient of the treatment group variable is −0.038, but is not statistically significant. Meanwhile, the coefficient of the treatment period variable is −0.117 and is statistically significant at the 1% level. This means that during the experimental period, all households had a tendency to use 11.7% less electric energy than during the pre-experimental period. In particular, the average treatment effect is identified as −0.138 and is statistically significant at the 10% level.

There is a consistency between this result and the first hypothesis that the dynamic pricing is effective in curtailing the energy demand of consumers. To be specific, the households reduce their electric energy by 13.8%, compared to the pre-experimental period. As mentioned in the literature <span id="page-11-0"></span>review, previous studies also found a demand-constrained effect in the first trial; the hypothesis was confirmed as consistent with the findings of previous studies.

| Before the Inverse Change between the Two Groups   |                                           |
|----------------------------------------------------|-------------------------------------------|
| Summer Treatment Effect                            | Summer Habit Formation                    |
| Treatment group                                    | -0.037<br>(0.099)                         |
| -0.038<br>(0.098)                                  | Treatment group                           |
| Treatment period                                   | -0.159 ***<br>(0.023)                     |
| -0.117 ***<br>(0.021)                              | Post-treatment period                     |
| Average treatment effect<br>(interaction variable) | -0.141 *<br>(0.073)                       |
| -0.138 *<br>(0.077)                                | Habit formation<br>(interaction variable) |
| R-squared                                          | 0.394                                     |
| 0.378                                              | R-squared                                 |
| Observations                                       | 18,187                                    |
| 18,187                                             | Observations                              |
| Number of households                               | 44                                        |
| 44                                                 | Number of households                      |

**Table 5.** Summer experiment's regression results.

Notes: Robust standard errors in brackets, \*\*\* *p* < 0.01, \*\* *p* < 0.05, \* *p* < 0.1. See full estimated results in Table [A1](#page-18-0) in Appendix [A.](#page-17-0)

Besides the main variables of DID, frequency of access is also one variable of interest. As hypothesized, since feedback technologies should help consumers recognize their consumption and efforts of saving energy, the more they access the visualization website, the less they consume. However, the regression result does not show that effect on consumption (Table [A1](#page-18-0) in Appendix [A\)](#page-17-0). The data suggest that households who consume more tend to check on the visualization system 9.2%–10.7% more than the rest of the households. This positive effect is totally opposite to the expectation that the more frequently households access the visualization system, the more strongly demand-constrained effect is stimulated. Nevertheless, dynamic pricing as a subsidiary factor that has the potential to reduce energy demand in summer is supported.

Regarding other factors that influence electric energy consumption of the households, the positive impacts of weather factors on energy consumption behavior are not statistically significant. Especially, even though the experiment was conducted in summer, the coefficient of cooling-degrees does not show any effect on consumption. In other words, participants may have experienced a cool summer.

Life-style factors also display insignificant negative marginal effects on consumption in the daytime period from 7 a.m. to 9 p.m. However, in the afternoon and evening from 4 p.m. to 9 p.m., households tend to increase their consumption by 37.7%–46.8%. This may not be unusual, since this time is peak-time, when people get home and gather around tables. The correlation between the predicted and actual usage during the summer experiment period is shown in Figure [A1](#page-20-1) in Appendix [A.](#page-17-0)

### *3.2. Habit Formation*

As discussed in the hypotheses and empirical models sections, this investigation set out to find evidence of habit formation in the winter experiment, as well as in the extension part of the summer experiment. The habit formation here is defined as the behavior to continue controlling electric energy demand, even after the treatment was removed. Supportive data for that behavior first can be found from the right-hand column of Table [1.](#page-6-0) This column presents the result of model (2) in which the interaction term between treatment group and post-treatment period shows a statistically significant coefficient of −0.141. It means that a demand-constrained effect still remains in the post-experimental period amounting to 14.1% of reduction, even larger than the effect during the experiment period.

Moreover, further evidence of habit formation appears in the winter trial, which is shown in Table [6.](#page-12-0) The left-hand column of Table [6](#page-12-0) shows the three main coefficients of interest. Unlike the summer's result, both the treatment group and treatment period variables suggest positive statistically significant coefficients.

<span id="page-12-0"></span>

| After the Inverse Change between the Two Groups    |                        |
|----------------------------------------------------|------------------------|
| Winter Treatment Effect                            | Winter Habit Formation |
| Treatment group                                    | 0.217 *<br>(0.121)     |
| Treatment group                                    | 0.220 *<br>(0.122)     |
| Treatment period                                   | 0.079 **<br>(0.033)    |
| Post-treatment period                              | 0.017<br>(0.031)       |
| Average treatment effect<br>(interaction variable) | -0.095<br>(0.096)      |
| Habit formation<br>(interaction variable)          | -0.080<br>(0.113)      |
| R-squared                                          | 0.272                  |
| R-squared                                          | 0.271                  |
| Observations                                       | 32,893                 |
| Observations                                       | 32,880                 |
| Number of households                               | 43                     |
| Number of households                               | 43                     |

**Table 6.** Winter experiment's regression results.

Notes: Robust standard errors in brackets, \*\*\* *p* < 0.01, \*\* *p* < 0.05, \* *p* < 0.1. See full estimated results in Table [A2](#page-19-0) in Appendix [A.](#page-17-0)

For an easier understanding, dynamic pricing effects in the summer and winter are graphically described in Figure [6.](#page-12-1) The treatment group in the summer is denoted as group A, and the other is indicated as group B. *Energies* **2016**, *9*, 1093 13 of 21

<span id="page-12-1"></span>Image /page/12/Figure/5 description: The image shows two graphs comparing the treatment and control groups in the summer and winter trials. In the summer trial, the control group is labeled as 'B' and the treatment group is labeled as 'A'. The graph shows that the control group's value remains relatively constant over time, while the treatment group's value decreases over time. In the winter trial, the treatment group is labeled as 'Treatment group' and the control group is labeled as 'Control group'. The graph shows that both the treatment and control groups' values increase over time, but the treatment group's value increases more than the control group's value. The difference between the treatment and control groups' values is labeled as 'YB-YB-1' and 'YA-YA-1'.

**Figure 6.** DID: Graphic depiction of treatment outcomes. **Figure 6.** DID: Graphic depiction of treatment outcomes.

As shown in Figure 6 on the left, in the summer trial, there was initially hardly any difference in consumption between the two groups (since the coefficient of treatment group variable is not statistically significant). However, it was after undergoing the treatment that the summer treatment group (group A) reduced electric energy usage more than group B. Therefore, the treatment group variable's positive coefficient (0.217) in the winter trial supports the hypothesis of habit formation. Specifically, the winter treatment group (group B) generally has a 21.7% larger consumption than group A. In the winter trial, the treatment period variable also has a significant positive coefficient of As shown in Figure [6](#page-12-1) on the left, in the summer trial, there was initially hardly any difference in consumption between the two groups (since the coefficient of treatment group variable is not statistically significant). However, it was after undergoing the treatment that the summer treatment group (group A) reduced electric energy usage more than group B. Therefore, the treatment group variable's positive coefficient (0.217) in the winter trial supports the hypothesis of habit formation. Specifically, the winter treatment group (group B) generally has a 21.7% larger consumption than group A.

0.079. This data suggests that both groups tended to increase their consumption by 7.9% in comparison with the two weeks prior to the winter intervention. In the winter, it may be difficult for the participants of both groups to conserve electric energy used to warm their houses and maintain domestic comfort, especially during the peak periods of the evening and the early morning. There was a sudden coincident drop in the ambient temperature during the two weeks of the experiment in comparison with the pre-experimental period (see Figure 7). This finding is consistent with what Wolak [7] (p. 87) found in his study, noting that dynamic pricing effects in the winter tended to be In the winter trial, the treatment period variable also has a significant positive coefficient of 0.079. This data suggests that both groups tended to increase their consumption by 7.9% in comparison with the two weeks prior to the winter intervention. In the winter, it may be difficult for the participants of both groups to conserve electric energy used to warm their houses and maintain domestic comfort, especially during the peak periods of the evening and the early morning. There was a sudden coincident drop in the ambient temperature during the two weeks of the experiment in comparison with the pre-experimental period (see Figure [7\)](#page-13-0). This finding is consistent with what Wolak [\[7\]](#page-21-5)

"far less precisely estimated".

<span id="page-13-0"></span>(p. 87) found in his study, noting that dynamic pricing effects in the winter tended to be "far less precisely estimated". Wolak [7] (p. 87) found in his study, noting that dynamic pricing effects in the winter tended to be "far less precisely estimated".

Image /page/13/Figure/2 description: The image is a line graph showing the average temperature in degrees Celsius from January 1st to February 1st. The x-axis represents the date, starting from January 1st and ending on February 1st. The y-axis represents the average temperature in degrees Celsius, ranging from -2 to 12. The line graph shows the temperature fluctuations over the period. From January 1st to January 6th, the temperature is relatively high, ranging from 9 to 10 degrees Celsius. From January 7th to January 17th, the temperature gradually decreases, reaching a low of around 5 degrees Celsius. From January 18th to January 24th, the temperature drops sharply, reaching a low of around -1 degree Celsius. From January 25th to January 31st, the temperature gradually increases, reaching a high of around 8 degrees Celsius. The graph also includes a horizontal dashed line at -0.5 degrees Celsius and a vertical dashed line at January 19th.

**Figure 7.** Average daily temperature of the pre-experimental and experimental periods in the winter 2016. Source: Japan Meteorological Agency, Climate Statistic[s \[1](#page-21-17)9]. **Figure 7.** Average daily temperature of the pre-experimental and experimental periods in the winter 2016. Source: Japan Meteorological Agency, Climate Statistics [19].

However, the more important finding is that the average treatment effect's coefficient no longer shows a statistically significant value (−0.095). As noted in the preceding sections, there was an inverse change between the control group and the treatment group. Even though both groups could not curtail their consumption, this regression result reveals that the summer treatment group could maintain their electric energy usage's fluctuation at about the same level as the winter treatment However, the more important finding is that the average treatment effect's coefficient no longer shows a statistically significant value (−0.095). As noted in the preceding sections, there was an inverse change between the control group and the treatment group. Even though both groups could not curtail their consumption, this regression result reveals that the summer treatment group could maintain their electric energy usage's fluctuation at about the same level as the winter treatment group could (in Figure [6,](#page-12-1) *Y* B *t* <sup>0</sup> − *Y* B *t* <sup>0</sup>−<sup>1</sup> ≈ *Y* A *t* <sup>0</sup> − *Y* A *t* <sup>0</sup>−1). It may be assumed that group A may have had significantly larger electric energy usage, if their habits of controlling electric energy usage had not been sustained. In other words, the hypothesis that the former treatment group still maintains their energy-saving habits is supported.

In addition, the energy-saving habits of the former treatment group have been sustained throughout the winter post-experimental period as well. This hypothesis was supported by the interaction coefficient's statistical insignificance displayed in the right-hand column of Table [6.](#page-12-0)

Further details of other factors having impacts on the winter's consumption are explained by the full results of model (3) and (4) in Table [A2](#page-19-0) in Appendix [A.](#page-17-0) From both models, the basic control variables of weather factors show a strong influence on energy demand. Concretely, a 1% increase in heating-degrees brings about an increase of 1.2%–1.7% in energy consumption, which is significant and larger than that observed in summer. In addition, the variable of average wind speed maintained its robustness in all models and brings about a 1.3%–2.2% increase in energy demand.

In winter, the contribution of life-style factors to the fluctuation of energy consumption is nearly the same as in summer (varies from 30.4% to 41.4% in peak period). In the off-peak period, life-style factors show insignificantly negative coefficients, which vary from −1.1% to −11.6%.

### *3.3. Price Elasticity of Demand*

As explained in the empirical model section, in the cases in which households respond to the marginal changes of deduction rates, the energy-saving effects of the 40-point-rate should be the largest, and those of the 20-point-rate should be the smallest. However, based on the regression results of model (5), (6), and (7) (Table [A3](#page-20-2) in Appendix [A\)](#page-17-0), and the figure below, any evidence for price elasticity of demand cannot be found. Figure [8](#page-14-0) describes the relation between the deduction rate and the energy-saving effect. Energy-saving effects were calculated by multiplying the coefficient β1 in model (5), (6), and (7) by negative 100.

<span id="page-14-0"></span>Image /page/14/Figure/1 description: The figure shows a line graph of consumers' reaction to deduction rate. The x-axis is the deduction rate, and the y-axis is the energy-saving effect in percentage. The graph shows that as the deduction rate increases, the energy-saving effect decreases. At a deduction rate of 20, the energy-saving effect is 18%. At a deduction rate of 30, the energy-saving effect is 10.6%. At a deduction rate of 40, the energy-saving effect is 3%.

**Figure 8.** Consumers' reaction to marginal changes of deduction rate. **Figure 8.** Consumers' reaction to marginal changes of deduction rate.

At first glance, it might appear from Figure 8 that there is a linear relation between the deduction rate and an energy-saving effect, which signifies that households might follow the price elasticity of demand. However, since all participants were allocated 7000 points at the beginning of the treatment, assuming that each household was given 500 points per day during the experimental period, deduction points could be considered to have the same effect as tariffs. Concretely, it means price elasticity of demand does not exist, unless there is a positive correlation between the deduction rate and energy-saving effects. In other words, an upward sloping consumer reaction line in Figure 8 would be expected. Based on the findings of the dynamic pricing effect in the previous sections, this evidence suggests that the consumers might respond to an average final incentive payment as a whole, rather than to marginal changes of the deduction rate. At first glance, it might appear from Figure [8](#page-14-0) that there is a linear relation between the deduction rate and an energy-saving effect, which signifies that households might follow the price elasticity of demand. However, since all participants were allocated 7000 points at the beginning of the treatment, assuming that each household was given 500 points per day during the experimental period, deduction points could be considered to have the same effect as tariffs. Concretely, it means price elasticity of demand does not exist, unless there is a positive correlation between the deduction rate and energy-saving effects. In other words, an upward sloping consumer reaction line in Figure [8](#page-14-0) would be expected. Based on the findings of the dynamic pricing effect in the previous sections, this evidence suggests that the consumers might respond to an average final incentive payment as a whole, rather than to marginal changes of the deduction rate.

This insight seems to be different from what Shimada et al. [13] observed during the first experiment conducted in 2014. Table 7, which is cited from [13], displays the estimated energy-This insight seems to be different from what Shimada et al. [\[13\]](#page-21-11) observed during the first experiment conducted in 2014. Table [7,](#page-14-1) which is cited from [\[13\]](#page-21-11), displays the estimated energy-savings in Minami District. It demonstrates that when the frequency of access to tablet PCs is double the average or more, the energy-saving effect positively correlates with the deduction rate. Nonetheless, the results reported in the study of Shimada et al. [\[13\]](#page-21-11) are based on the first experiment carried out in Nushima, in when habit formation had not yet occurred. In other words, at that time the participants have not reached the limit of constraining their demand. However, once habit formation occurs and it comes to the point at which consumers have to face the trade-off between energy conservation and their surplus, it requires an extremely strenuous effort to curtail load even more. The experiment in our study may have reached that point. When it comes to the limit of energy-serving effort, consumers may pursue their surplus effortlessly on sunny days rather than restrict their consumption on rainy days, regardless of the deduction rate. That explains why the consumers' reaction line in Figure [8](#page-14-0) is downward sloping.

| Deduction Rate | Frequency of Viewing Tablet PC Per Day |      |       |       |
|----------------|----------------------------------------|------|-------|-------|
|                | 0                                      | 1    | 2     | 3     |
| 20             | -5.2%                                  | 1.7% | 5.8%  | 8.7%  |
| 30             | -0.9%                                  | 6.0% | 10.0% | 12.8% |
| 40             | -8.6%                                  | 5.4% | 13.5% | 19.3% |

<span id="page-14-1"></span>**Table 7.** Estimated energy-saving effect in Minami District. Source: Shimada et al. [\[13\]](#page-21-11).

Regarding the elasticity of demand to price, there has been a divergence among research conducted so far. Our finding is consistent with what Ito [\[20\]](#page-21-18) finds in his study. He claims that electric energy consumers in California adjust their consumption based on the average price of their electricity bills, rather than on the marginal changes in their price schedules. Meanwhile, the Shimada et al. [\[13\]](#page-21-11) study's finding is consistent with the experiment's results in Keihanna City of Ito et al. [\[12\]](#page-21-10), which indicates that as long as consumers received noticeable price information, they responded to time-variant marginal prices. While the experiment in Keihanna changed marginal prices over the course of a day, the study of Ito [\[20\]](#page-21-18) adjusted the price through monthly bills, and this study determined deduction rates based on the daily weather forecast. Since all those studies have different objects, designs, and methodologies (see Table [8\)](#page-15-0), it is not certain which insight is more appropriate.

<span id="page-15-0"></span>

| Study                         | Objects                                                                                                                       | Design Methodology                                                                                                 | Findings                                                                                                                                                                          | Differences of<br>This Study                                 |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| Shimada et al.<br>(2015) [13] | Assess the possibility<br>of solar photovoltaic<br>generation's<br>dynamic pricing                                            | Pre- and post-test<br>design, dynamic<br>pricing based on daily<br>weather forecast                                | Load-curtailing effects of<br>20% for real-time feedback<br>and 2% for<br>dynamic pricing                                                                                         | Group division                                               |
| Ito et al. (2015) [12]        | Investigate the<br>persistence of the<br>effects of moral<br>suasion and<br>economic incentive<br>on electric<br>energy usage | Randomized<br>controlled trial design,<br>hourly critical peak<br>pricing (CPP)                                    | Usage reduction of moral<br>suasion is 8% but not<br>persistent. Usage<br>reduction of economic<br>incentive is 14% for the<br>lowest CPP, 17% for the<br>highest, and persistent | Dynamic pricing<br>using daily<br>deduction rate,<br>not CPP |
| Ito (2014) [20]               | Assess whether<br>households respond<br>to marginal or<br>average price                                                       | Panel analysis using<br>household-level<br>monthly data of all<br>households in<br>California from 1999<br>to 2007 | Consumers do not respond<br>to expected marginal price,<br>but average price                                                                                                      | Randomized<br>controlled trial,<br>dynamic pricing           |

#### **Table 8.** Studies' comparison.

## **4. Policy Implications**

At the hypothesizing stage of this study, there are two kinds of policy that would have potential for electric energy demand management at the household level, in remote islands where solar photovoltaic generation is considered for utilization. One policy is adjusting marginal price in accordance with energy-generating capacity, which fluctuates due to the weather or solar radiation of a day. The other policy is having consumers form energy-saving habits by letting them undertake a treatment, which provides an incentive payment for a while. In fact, this experiment is the combination of these two policies over a short time of two weeks.

On one hand, habit formation which is confirmed in the post-experimental periods hints at an approach to turn energy efficiency and conservation into consumers' daily life styles. This policy requires an initial investment in smart meters and feedback technologies, and incentive payments during trial periods. However, since the energy-saving habits once formed are sustainable, this policy can be applied for a small and remote community like Nushima Island, where electric energy supply is volatile due to the market liberalization.

On the other hand, it still remains unexplained what kind of dynamic pricing design is appropriate for the price elasticity of electric energy demand. This kind of intervention should be a short-term means to provide a hook of habit formation, since consumers cannot curtail consumption when it comes to their limit. Once habit formation is confirmed, the intervention should be cancelled or be loosened. Nevertheless, whether habit formation occurs even after withdrawing interventions or not also depends on the culture and characteristics of the consumers and regions. For instance, since a major proportion of the households in Nushima use only electricity as their domestic energy, they have a strong incentive to reduce their electric energy usage. These characteristics may not apply to other areas. Therefore, the determination of the intervention's duration should be taken discreetly in accordance with other regional characteristics.

<span id="page-16-0"></span>

## **5. Conclusions**

Although the so-called dynamic pricing through real-time information feedback has been studied in several field experiments so far, this study explores its potential using the perspective of remote islands which attempt to utilize solar resources as a basis for energy policy.

As discussed in the theoretical framework, a demand response system helps not only electric energy suppliers but also their consumers to achieve better ends, while promoting renewable energy and energy conservation to mitigate global warming. The regression results of Section [5](#page-16-0) also suggest that the dynamic pricing is effective in constraining the energy demand of consumers by reducing their electric energy usage by 13.8%. However, in opposition to the expectation that the more frequently households access the visualization system, the more strongly the demand-constrained effect is stimulated, the result is that households tend to increase their consumption by 9.2%–10.7% per time of access.

Using the new approach to verify habit formation or persistence of dynamic pricing by demonstrating an inverse change between the control and treatment groups in the second trial, the results confirm that the intervention is persistent and energy-saving habits were firmly formed among participants of the initial treatment group. Since the two groups had an inverse change between each other, the insignificant coefficient of DID implies that even though the winter treatment group underwent the treatment, they could not curtail consumption by less than the former treatment group's consumption; thus the former treatment group still retains their energy-saving habits.

Regarding the responses of the households to change their deduction rates, the result is not consistent with the hypothesis of demand elasticity to price. The regression results suggest that the consumers respond to an average final incentive payment as a whole, rather than to marginal changes of deduction rate.

The findings on dynamic pricing effects, habit formation and households' reaction toward deduction rates shed some light on policy implications for remote islands. Specifically, this load-curtailing intervention, which is accompanied with incentive payments, has potential in creating a policy shock that leads to consumers forming energy-serving habit.

**Acknowledgments:** This work was supported by JSPS Grant No. 15K00645. We appreciate the support of the Ministry of Environment of Japan through the technological development and demonstration research project for global warming countermeasures. We also thank Kei Sakata of Ritsumeikan University for his academic support to our research.

**Author Contributions:** Koji Shimada, Yuki Ochi, Takuya Matsumoto, Hiroshi Matsugi and Takao Awata conceived, designed and performed the experiments; Thoa Thi Kim Nguyen and Koji Shimada analyzed the data; Thoa Thi Kim Nguyen mainly wrote the paper.

**Conflicts of Interest:** The authors declare no conflict of interest.

### **Nomenclature**

| Ln_elec_con  | Hourly electric energy consumption (Wh); Source: Smart meter    |
|--------------|-----------------------------------------------------------------|
| Cool_d       | Cooling degrees (°); Source: Japan Meteorological Agency [19]   |
| Heat_d       | Heating degrees (°); Source: Same above [19]                    |
| Wind         | Hourly mean wind speed (m/s)                                    |
| Period_n     | Dummy variable for each time period (3 h interval)              |
| Access times | Frequency of access to tablet PC (times/h); Source: Smart meter |
| Member       | Household member (person); Source: Survey                       |
| District_n   | Regional dummies (District 1-4); Source: Survey                 |
| Happye       | Happye dummy (discount after 10 p.m.); Source: Survey           |
| Aircon       | Air-conditioner (unit); Source: Survey                          |
| Fridge       | Number of fridge (unit); Source: Survey                         |
| Com_fridge   | Number of commercial refrigerator (unit); Source: Survey        |
| Wood         | Wooden house dummy; Source: Survey                              |
| 20_p         | 20-point deduction day dummy                                    |
| 30_p         | 30-point deduction day dummy                                    |
| 40_p         | 40-point deduction day dummy                                    |

#### **DID Variables**

| Treat-period (summer)            | Pre-experimental period = 0 (28-31 August);<br>Experimental period = 1 (1-14 September)        |
|----------------------------------|------------------------------------------------------------------------------------------------|
| Treat-period (winter)            | Pre-experimental period = 0 (1-18 January);<br>Experimental period = 1 (19 January-1 February) |
| Treat-group                      | Control group = 0 ;Treatment group = 1                                                         |
| Treat-effect                     | = Treat-period × Treat-group                                                                   |
| Post-treat-period (summer)       | Pre-experimental period = 0 (28-31 August);<br>Post-experimental period = 1 (15-30 September)  |
| Post-treat-period (winter)       | Pre-experimental period = 0 (1-18 January);<br>Post-experimental period = 1 (2-15 February)    |
| Habit formation                  | = Post-Treat-period × Treatgroup                                                               |
| Treat-effect-period_n dummy      | = Treat-effect × Period_n                                                                      |
| Post-treat-effect-period_n dummy | = Post-treat-effect × Period_n                                                                 |
| 20p_elas                         | = 20_p × Treat-group                                                                           |
| 30p_elas                         | = 30_p × Treat-group                                                                           |
| 40p_elas                         | = 40_p × Treat-group                                                                           |

<span id="page-17-0"></span>

#### **Appendix A**

**Table A1.** Full regression results of the summer's experiment.

| Natural Logarithm of Hourly Electric Energy Consumption |                                                          |
|---------------------------------------------------------|----------------------------------------------------------|
| Summer Treatment Effect—Model (1)                       | Summer Habit Formation—Model (2)                         |
| Treat-group<br>(0.098)                                  | -0.038<br>Treat-group<br>-0.037<br>(0.099)               |
| Treat-period<br>(0.021)                                 | -0.117 ***<br>Post-treat-period<br>-0.159 ***<br>(0.023) |
| Treat-effect<br>(0.077)                                 | -0.138 *<br>Habit formation<br>-0.141 *<br>(0.073)       |
| Treat-period_1 (1–3 h)<br>(0.108)                       | 0.141<br>Post-treat-period_1<br>0.156<br>(0.098)         |
| Treat-period_2 (4–6 h)<br>(0.099)                       | 0.168 *<br>Post-treat-period_2<br>0.221 **<br>(0.092)    |
| Treat-period_3 (7–9 h)<br>(0.086)                       | -0.003<br>Post-treat-period_3<br>-0.015<br>(0.091)       |
| Treat-period_4 (10–12 h)<br>(0.105)                     | 0.025<br>Post-treat-period_4<br>-0.007<br>(0.104)        |
| Treat-period_5 (13−15 h)<br>(0.090)                     | 0.041<br>Post-treat-period_5<br>-0.001<br>(0.097)        |
| Treat-period_6 (16−18 h)<br>(0.104)                     | 0.468 ***<br>Post-treat-period_6<br>0.423 ***<br>(0.102) |
| Treat-period_7 (19−21 h)<br>(0.071)                     | 0.378 ***<br>Post-treat-period_7<br>0.366 ***<br>(0.073) |
| Wind<br>(0.004)                                         | 0.005<br>Wind<br>-0.003<br>(0.005)                       |
| Cool_d<br>(0.010)                                       | 0.003<br>Cool_d<br>0.000<br>(0.011)                      |
| Heat_d<br>(0.035)                                       | -0.033<br>Heat_d<br>-0.044 ***<br>(0.016)                |
| Access times<br>(0.040)                                 | 0.107 ***<br>Access times<br>0.092 ***<br>(0.030)        |
| Member<br>(0.035)                                       | 0.083 **<br>Member<br>0.077 **<br>(0.034)                |
| Happye<br>(0.096)                                       | 0.320 ***<br>Happye<br>0.316 ***<br>(0.095)              |

<span id="page-18-0"></span>

| Natural Logarithm of Hourly Electric Energy Consumption |                                  |              |                      |
|---------------------------------------------------------|----------------------------------|--------------|----------------------|
| Summer Treatment Effect—Model (1)                       | Summer Habit Formation—Model (2) |              |                      |
| Aircon                                                  | -0.003<br>(0.069)                | Aircon       | -0.002<br>(0.070)    |
| Fridge                                                  | 0.342 ***<br>(0.099)             | Fridge       | 0.357 ***<br>(0.090) |
| Com_fridge                                              | 0.346 ***<br>(0.081)             | Com_fridge   | 0.353 ***<br>(0.080) |
| Wood                                                    | 0.052<br>(0.104)                 | Wood         | 0.044<br>(0.113)     |
| District 1                                              | -0.086<br>(0.181)                | District 1   | -0.137<br>(0.180)    |
| District 2                                              | -0.028<br>(0.170)                | District 2   | -0.051<br>(0.168)    |
| District 3                                              | 0.096<br>(0.158)                 | District 3   | 0.071<br>(0.159)     |
| District 4                                              | -0.226<br>(0.183)                | District 4   | -0.295<br>(0.184)    |
| Constant                                                | 5.327 ***<br>(0.243)             | Constant     | 5.373 ***<br>(0.245) |
| R-squared                                               | 0.378                            | R-squared    | 0.394                |
| Observations                                            | 18,187                           | Observations | 18,187               |
| Number of ID                                            | 44                               | Number of ID | 44                   |

**Table A1.** *Cont.*

Notes: Robust standard errors in brackets, \*\*\* *p* < 0.01, \*\* *p* < 0.05, \* *p* < 0.1.

**Table A2.** Full regression results of the winter's experiment.

| Natural Logarithm of Hourly Electric Energy Consumption |                      |                                  |                      |
|---------------------------------------------------------|----------------------|----------------------------------|----------------------|
| Winter Treatment Effect—Model (3)                       |                      | Winter Habit Formation—Model (4) |                      |
| Treat-group                                             | 0.217 *<br>(0.121)   | Treat-group                      | 0.220 *<br>(0.122)   |
| Treat-period                                            | 0.079 **<br>(0.033)  | Post-treat-period                | 0.017<br>(0.031)     |
| Treat-effect                                            | −0.095<br>(0.096)    | Habit formation                  | −0.080<br>(0.113)    |
| Treat-period_1 (1–3 h)                                  | −0.094<br>(0.111)    | Post-treat-period_1              | −0.042<br>(0.127)    |
| Treat-period_2 (4–6 h)                                  | 0.066<br>(0.109)     | Post-treat-period_2              | 0.116<br>(0.113)     |
| Treat-period_3 (7–9 h)                                  | −0.049<br>(0.114)    | Post-treat-period_3              | −0.081<br>(0.137)    |
| Treat-period_4 (10–12 h)                                | −0.049<br>(0.123)    | Post-treat-period_4              | −0.074<br>(0.138)    |
| Treat-period_5 (13–15 h)                                | −0.011<br>(0.116)    | Post-treat-period_5              | −0.056<br>(0.131)    |
| Treat-period_6 (16–18 h)                                | 0.414 ***<br>(0.101) | Post-treat-period_6              | 0.381 ***<br>(0.105) |
| Treat-period_7 (19–21 h)                                | 0.310 ***<br>(0.097) | Post-treat-period_7              | 0.304 ***<br>(0.098) |

<span id="page-19-0"></span>

| Winter Treatment Effect—Model (3) |                      | Winter Habit Formation—Model (4) |                      |
|-----------------------------------|----------------------|----------------------------------|----------------------|
| Wind                              | 0.022 ***<br>(0.004) | Wind                             | 0.013 ***<br>(0.004) |
| Heat_d                            | 0.017 ***<br>(0.006) | Heat_d                           | 0.012 ***<br>(0.004) |
| Access times                      | 0.028<br>(0.057)     | Access times                     | -0.011<br>(0.078)    |
| Member                            | 0.107 **<br>(0.050)  | Member                           | 0.108 **<br>(0.047)  |
| Happye                            | 0.481 ***<br>(0.100) | Happye                           | 0.469 ***<br>(0.090) |
| Aircon                            | -0.006<br>(0.083)    | Aircon                           | -0.0201<br>(0.080)   |
| Fridge                            | 0.406 ***<br>(0.131) | Fridge                           | 0.422 ***<br>(0.128) |
| Com_fridge                        | 0.213 *<br>(0.110)   | Com_fridge                       | 0.194 *<br>(0.101)   |
| Wood                              | 0.061<br>(0.108)     | Wood                             | 0.0241<br>(0.093)    |
| District 1                        | -0.009<br>(0.254)    | District 1                       | -0.063<br>(0.258)    |
| District 2                        | 0.157<br>(0.243)     | District 2                       | 0.121<br>(0.244)     |
| District 3                        | 0.210<br>(0.228)     | District 3                       | 0.168<br>(0.228)     |
| District 4                        | -0.063<br>(0.253)    | District 4                       | -0.103<br>(0.255)    |
| Constant                          | 4.806 ***<br>(0.336) | Constant                         | 4.970 ***<br>(0.338) |
| Overall R squared                 | 0.272                | Overall R squared                | 0.271                |
| Observations                      | 32,893               | Observations                     | 32,880               |
| Number of ID                      | 43                   | Number of ID                     | 43                   |

### **Table A2.** *Cont.*

Notes: Robust standard errors in brackets, \*\*\* *p* < 0.01, \*\* *p* < 0.05, \* *p* < 0.1.

**Table A3.** Price elasticity of demand regression results.

| Natural Logarithm of Daily Electric Energy Consumption |                                   |                                     |
|--------------------------------------------------------|-----------------------------------|-------------------------------------|
| Model (5)                                              | Model (6)                         | Model (7)                           |
| 20p_elas<br>-0.179 ***<br>(0.035)                      | 30p_elas<br>-0.106 ***<br>(0.034) | 40p_elas<br>-0.032<br>(0.033)       |
| Wind<br>-0.028<br>(0.018)                              | Wind<br>0.005<br>(0.013)          | Wind<br>-0.041 ***<br>(0.009)       |
| Cool_d<br>0.003 **<br>(0.001)                          | Cool_d<br>0.003 **<br>(0.001)     | Cool_d<br>0.004 ***<br>(0.001)      |
| Access times<br>0.034<br>(0.029)                       | Access times<br>0.010<br>(0.007)  | Access times<br>0.040 **<br>(0.017) |

<span id="page-20-2"></span>

| Natural Logarithm of Daily Electric Energy Consumption |                      |                                    |                                    |
|--------------------------------------------------------|----------------------|------------------------------------|------------------------------------|
| Model (5)                                              | Model (6)            | Model (7)                          |                                    |
| Member                                                 | 0.081 ***<br>(0.031) | Member<br>0.080 **<br>(0.033)      | Member<br>0.100 ***<br>(0.036)     |
| Happye                                                 | 0.363 ***<br>(0.094) | Happye<br>0.376 ***<br>(0.091)     | Happye<br>0.411 ***<br>(0.090)     |
| Aircon                                                 | -0.003<br>(0.062)    | Aircon<br>-0.012<br>(0.060)        | Aircon<br>-0.017<br>(0.066)        |
| Fridge                                                 | 0.358 ***<br>(0.096) | Fridge<br>0.336 ***<br>(0.095)     | Fridge<br>0.312 ***<br>(0.100)     |
| Com_fridge                                             | 0.304 ***<br>(0.082) | Com_fridge<br>0.320 ***<br>(0.082) | Com_fridge<br>0.320 ***<br>(0.085) |
| Wood                                                   | 0.030<br>(0.119)     | Wood<br>0.060<br>(0.116)           | Wood<br>0.034<br>(0.119)           |
| District 1                                             | -0.137<br>(0.172)    | District1<br>-0.119<br>(0.161)     | District 1<br>-0.087<br>(0.171)    |
| District 2                                             | -0.060<br>(0.167)    | District2<br>-0.021<br>(0.158)     | District 2<br>0.025<br>(0.162)     |
| District 3                                             | 0.036<br>(0.152)     | District3<br>0.0552<br>(0.145)     | District 3<br>0.139<br>(0.153)     |
| District 4                                             | -0.277<br>(0.183)    | District4<br>-0.244<br>(0.165)     | District 4<br>-0.142<br>(0.172)    |
| Constant                                               | 8.571 ***<br>(0.231) | Constant<br>8.555 ***<br>(0.212)   | Constant<br>8.527 ***<br>(0.235)   |
| R squared                                              | 0.636                | R squared<br>0.634                 | R squared<br>0.589                 |
| Observations                                           | 349                  | Observations<br>307                | Observations<br>481                |
| Number of ID                                           | 44                   | Number of ID<br>44                 | Number of ID<br>44                 |

**Table A3.** *Cont.* 20p\_elas <sup>−</sup>0.179 \*\*\* 30p\_elas −0.106 \*\*\* 40p\_elas −0.032 (0.035) (0.034) (0.033)

<span id="page-20-1"></span>Notes: Robust standard errors in brackets, \*\*\* *p* < 0.01, \*\* *p* < 0.05, \* *p* < 0.1. Notes: Robust standard errors in brackets, \*\*\* *p* < 0.01, \*\* *p* < 0.05, \* *p* < 0.1.

Image /page/20/Figure/5 description: The image shows the title "Predicted and Actual Hourly Electric Energy Usage - Model (1)".

Image /page/20/Figure/6 description: This figure is a scatter plot of predicted hourly electric energy usage (kWh) versus actual hourly electric energy usage (kWh). The x-axis represents the actual hourly electric energy usage (kWh), ranging from 0 to 5000. The y-axis represents the predicted hourly electric energy usage (kWh), ranging from 0 to 4000. The data points are clustered in two main groups. The first group is clustered around the y axis from 0 to 1000 and the x axis from 0 to 2500. The second group is clustered around the y axis from 3000 to 4000 and the x axis from 2500 to 4500.

**Figure A1.** The correlation between predicted and actual hourly usage in the summer experiment. **Figure A1.** The correlation between predicted and actual hourly usage in the summer experiment.

#### **References**

<span id="page-20-0"></span>1. About Nushima. Available online: <http://web-japan.org/kidsweb/meet/nushima/about02.html> (accessed on 7 July 2016).

- <span id="page-21-0"></span>2. Hyogo Prefecture Website. Available online: [https://web.pref.hyogo.lg.jp/awk01/furusatogakusyu/](https://web.pref.hyogo.lg.jp/awk01/furusatogakusyu/documents/1syo-5.pdf) [documents/1syo-5.pdf](https://web.pref.hyogo.lg.jp/awk01/furusatogakusyu/documents/1syo-5.pdf) (accessed on 30 June 2016).
- <span id="page-21-1"></span>3. Agency for Natural Resources and Energy. Available online: [http://www.enecho.meti.go.jp/category/](http://www.enecho.meti.go.jp/category/electricity_and_gas/electric/pdf/seido1206.pdf) [electricity\\_and\\_gas/electric/pdf/seido1206.pdf](http://www.enecho.meti.go.jp/category/electricity_and_gas/electric/pdf/seido1206.pdf) (accessed on 22 August 2015).
- <span id="page-21-2"></span>4. Greer, M. *Electricity Marginal Cost Pricing: Applications in Eliciting Demand Responses*; Butterworth-Heinemann: Waltham, MA, USA, 2012.
- <span id="page-21-3"></span>5. Faruqui, A.; Sergici, S. Household response to dynamic pricing of electricity: A survey of 15 experiments. *J. Regul. Econ.* **2010**, *38*, 193–225. [\[CrossRef\]](http://dx.doi.org/10.1007/s11149-010-9127-y)
- <span id="page-21-4"></span>6. Shadish, W.R.; Cook, T.D.; Campbell, D.T. *Experimental and Quasi-Experimental Designs for Generalized Causal Inference*; Houghton Mifflin: Boston, MA, USA, 2002.
- <span id="page-21-5"></span>7. Wolak, F.A. Do residential customers respond to hourly prices? Evidence from a dynamic pricing experiment. *Am. Econ. Rev.* **2011**, *101*, 83–87. [\[CrossRef\]](http://dx.doi.org/10.1257/aer.101.3.83)
- <span id="page-21-6"></span>8. Frey, E.; Rogers, T. Persistence: How treatment effects persist after interventions stop. *Policy Insights Behav. Brain Sci.* **2014**, *1*, 172–179. [\[CrossRef\]](http://dx.doi.org/10.1177/2372732214550405)
- <span id="page-21-7"></span>9. Khawaja, S.; Stewart, J. Long-Run Savings and Cost-Effectiveness of Home Energy Report Programs. Cadmus Group, 2014. Available online: [http://www.cadmusgroup.com/wp-content/uploads/2014/11/](http://www.cadmusgroup.com/wp-content/uploads/2014/11/Cadmus_Home_Energy_Reports_Winter2014.pdf) [Cadmus\\_Home\\_Energy\\_Reports\\_Winter2014.pdf](http://www.cadmusgroup.com/wp-content/uploads/2014/11/Cadmus_Home_Energy_Reports_Winter2014.pdf) (accessed on 6 July 2016).
- <span id="page-21-8"></span>10. Allcott, H.; Rogers, T. The short-run and long-run effects of behavioral interventions: Experimental evidence from energy conservation. *Am. Econ. Rev.* **2014**, *104*, 3003–3037. [\[CrossRef\]](http://dx.doi.org/10.1257/aer.104.10.3003)
- <span id="page-21-9"></span>11. Japan Smart City Reports. Available online: <http://jscp.nepc.or.jp/en/index.shtml> (accessed on 20 August 2015).
- <span id="page-21-10"></span>12. Ito, K.; Ida, T.; Tanaka, M. *The Persistence of Moral Suasion and Economic Incentives: Field Experimental Evidence from Energy Demand*; NBER Working Paper No. 20910; The National Bureau of Economic Research (NBER): Cambridge, MA, USA, 2015.
- <span id="page-21-11"></span>13. Shimada, K.; Ochi, Y.; Matsumoto, T.; Matsugi, H.; Awata, T. An Empirical Study of Real-time Feedback and Dynamic Pricing Effects on Electric Power Consumption—Field Experiment on a Remote Island in Japan. In Proceedings of the 4th International Conference on Smart Cities and Green ICT Systems, Lisbon, Portugal, 20–22 May 2015; pp. 201–208.
- <span id="page-21-12"></span>14. Torgerson, D.J.; Torgerson, C.J. *Designing Randomised Trials in Health, Education and the Social Sciences: An Introduction*; Palgrave Macmillan: Basingstoke, UK, 2008.
- <span id="page-21-13"></span>15. Faruqui, A.; Sergici, S. Dynamic pricing of electricity in the mid-Atlantic region: Econometric results from the Baltimore gas and electric company experiment. *J. Regul. Econ.* **2011**, *40*, 82–109. [\[CrossRef\]](http://dx.doi.org/10.1007/s11149-011-9152-5)
- <span id="page-21-14"></span>16. Jessoe, K.; Rapson, D. Knowledge is (Less) power: Experimental evidence from residential energy use. *Am. Econ. Rev.* **2014**, *104*, 1417–1438. [\[CrossRef\]](http://dx.doi.org/10.1257/aer.104.4.1417)
- <span id="page-21-15"></span>17. Becker, G.S.; Murphy, K.M. A theory of rational addiction. *J. Politcal Econ.* **1988**, *96*, 576–700. [\[CrossRef\]](http://dx.doi.org/10.1086/261558)
- <span id="page-21-16"></span>18. Kunst, R. Summary Based on Chapter 12 of Baltagi: Panel Unit Root Tests. Available online: [http://](http://homepage.univie.ac.at/robert.kunst/pan2011_pres_nell.pdf) [homepage.univie.ac.at/robert.kunst/pan2011\\_pres\\_nell.pdf](http://homepage.univie.ac.at/robert.kunst/pan2011_pres_nell.pdf) (accessed on 6 July 2016).
- <span id="page-21-17"></span>19. Japan Meteorological Agency. Climate Statistics. Available online: [http://www.data.jma.go.jp/obd/stats/](http://www.data.jma.go.jp/obd/stats/etrn/index.php?prec_no=63&block_no=1337&year=&month=&day=&view) [etrn/index.php?prec\\_no=63&block\\_no=1337&year=&month=&day=&view](http://www.data.jma.go.jp/obd/stats/etrn/index.php?prec_no=63&block_no=1337&year=&month=&day=&view) (accessed on 20 August 2015).
- <span id="page-21-18"></span>20. Ito, K. Do consumers respond to marginal or average price? Evidence from nonlinear electricity pricing. *Am. Econ. Rev.* **2014**, *104*, 537–563. [\[CrossRef\]](http://dx.doi.org/10.1257/aer.104.2.537)

Image /page/21/Picture/20 description: The image shows a Creative Commons Attribution license. The license is represented by the "CC" symbol inside a circle, and the "BY" symbol, which is a person icon inside a circle, indicating that the work can be used as long as attribution is given to the original author.

© 2016 by the authors; licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC-BY) license [\(http://creativecommons.org/licenses/by/4.0/\)](http://creativecommons.org/licenses/by/4.0/.).