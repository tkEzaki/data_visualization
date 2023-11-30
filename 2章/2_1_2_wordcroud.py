from wordcloud import WordCloud  # wordcloudパッケージをインポート
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib


# テキストデータ
text = "Clustering coefficients for correlation networks, Energy landscape analysis of neuroimaging data, Simulation of space acquisition process of pedestrians using proxemic floor field model, Pedestrian flow through multiple bottlenecks, Closer to critical resting-state neural dynamics in individuals with higher fluid intelligence, Reinforcement learning explains conditional cooperation and its moody cousin, Jam-absorption driving with a car-following model, Age‐related changes in the ease of dynamical transitions in human brain activity, Potential global jamming transition in aviation networks, Methodology and theoretical basis of forward genetic screening for sleep/wakefulness in mice, Jamming transitions in force-based models for pedestrian dynamics, Inflow process of pedestrians to a confined space, Exact solution of a heterogeneous multilane asymmetric simple exclusion process, Exact stationary distribution of an asymmetric simple exclusion process with Langmuir kinetics and memory reservoirs, Taming macroscopic jamming in transportation networks, A demonstration experiment of a theory of jam-absorption driving, A balance network for the asymmetric simple exclusion process, Reinforcement learning account of network reciprocity, Towards understanding network topology and robustness of logistics systems, Inflow process: A counterpart of evacuation, Analysis on a single segment of evacuation network, Dynamics of assembly production flow, Presynaptic inhibition of dopamine neurons controls optimistic bias, Bridging the micro-macro gap between single-molecular behavior and bulk hydrolysis properties of cellulase, Cluster size distribution in 1D-CA traffic models, Modelling state‐transition dynamics in resting‐state brain signals by the hidden Markov and Gaussian mixture models, Positive congestion effect on a totally asymmetric simple exclusion process with an adsorption lane, Metastability in pedestrian evacuation, Constructing quantum dark solitons with stable scattering properties, The Autonomous Sensory Meridian Response Activates the Parasympathetic Nervous System, Trait, staging, and state markers of psychosis based on functional alteration of salience-related networks in the high-risk, first episode, and chronic stages, Critical brain dynamics and human intelligence, Influence of velocity variance of a single particle on cellular automaton models, Collective motion of oscillatory walkers, Reinforcing critical links for robust network logistics: A centrality measure for substitutability, Dynamic transitions between brain states predict auditory attentional fluctuations, Associations of conservatism/jumping to conclusions biases with aberrant salience and default mode network, Model retraining and information sharing in a supply chain with long-term fluctuating demands, Functional alterations of salience-related networks are associated with traits, staging, and the state of psychosis."


# WordCloudオブジェクトを生成
wordcloud = WordCloud(
    relative_scaling=1,  # 文字の大きさを指定
    background_color="white",  # 背景色を指定
    colormap="jet",  # カラーマップを指定
    font_path='C://Windows//Fonts//ariblk.ttf',  # ご自身の環境によって設定して下さい
    width=1000,  # 横幅を指定
    height=500,  # 縦幅を指定
    random_state=12  # いい感じになるシードを選んだ
).generate(text)

# ワードクラウドを描画
plt.figure(figsize=(10, 5))  # 図のサイズを設定
plt.imshow(wordcloud)  # ワードクラウドを描画
plt.axis("off")  # 軸を非表示にする
plt.tight_layout()  # レイアウトを調整
plt.savefig("2_1_2_wordcloud.png", dpi=300)  # 画像を保存
plt.show()  # 画像を表示
