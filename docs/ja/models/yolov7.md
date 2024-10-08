---
comments: true
description: YOLOv7は高速性と精度の両方で既知の物体検出器を凌駕する最先端のリアルタイム物体検出器です。この技術では、モデル再パラメータ化、動的ラベル割り当て、拡張スケーリング、複合スケーリングなど、学習可能なBag-of-Freebies最適化に焦点を当てています。
keywords: YOLOv7, リアルタイム物体検出器, 最先端, Ultralytics, MS COCO データセット, モデル再パラメータ化, 動的ラベル割り当て, 拡張スケーリング, 複合スケーリング
---

# YOLOv7: 学習可能なBag-of-Freebies

YOLOv7は、5 FPSから160 FPSの範囲で、既知のすべての物体検出器を速度と精度の両方で凌駕する最先端のリアルタイム物体検出器です。GPU V100上で30 FPS以上の性能を持つリアルタイム物体検出器の中で、最高の精度（56.8% AP）を持っています。さらに、YOLOv7はYOLOR、YOLOX、Scaled-YOLOv4、YOLOv5などの他の物体検出器を速度と精度の面で上回っています。このモデルは、他のデータセットや事前学習重みを使用せずに、MS COCOデータセットでトレーニングされています。YOLOv7のソースコードはGitHubで入手できます。

![SOTA物体検出器との比較](https://github.com/ultralytics/ultralytics/assets/26833433/5e1e0420-8122-4c79-b8d0-2860aa79af92)
**最先端物体検出器との比較。** 表2の結果からわかるように、提案手法は速度と精度のトレードオフにおいて最も優れています。例えば、YOLOv7-tiny-SiLUとYOLOv5-N（r6.1）を比較すると、我々の手法は127 fps速く、APにおいて10.7%精度が向上しています。また、YOLOv7はフレームレート161 fpsで51.4%のAPを達成していますが、同じAPを持つPPYOLOE-Lのフレームレートは78 fpsのみです。パラメータ使用量に関しては、YOLOv7はPPYOLOE-Lよりも41%少ないです。さらに、114 fpsの推論速度を持つYOLOv7-Xを99 fpsの推論速度を持つYOLOv5-L（r6.1）と比較すると、YOLOv7-XはAPを3.9%向上させることができます。YOLOv7-Xをスケールの近いYOLOv5-X（r6.1）と比較すると、YOLOv7-Xの推論速度は31 fps速いです。また、パラメータ量と計算量の観点から、YOLOv7-XはYOLOv5-X（r6.1）に比べてパラメータを22%、計算量を8%削減していますが、APは2.2%向上しています（[出典](https://arxiv.org/pdf/2207.02696.pdf)）。

## 概要

リアルタイム物体検出は、マルチオブジェクトトラッキング、自動運転、ロボティクス、医療画像解析など、多くのコンピュータビジョンシステムの重要なコンポーネントです。近年、リアルタイム物体検出の開発は、さまざまなCPU、GPU、ニューラルプロセッシングユニット（NPU）の推論速度の効率的なアーキテクチャの設計と向上に焦点を当てています。YOLOv7は、エッジからクラウドまで、モバイルGPUとGPUデバイスの両方をサポートしています。

従来のリアルタイム物体検出器がアーキテクチャの最適化に焦点を当てるのに対し、YOLOv7では学習プロセスの最適化に注力しています。これには、推論コストを増やさずに物体検出の精度を向上させるためのモジュールや最適化手法が含まれます。これは、「学習可能なBag-of-Freebies」というコンセプトです。

## 主な特徴

YOLOv7は、いくつかの主な特徴を導入しています。

1. **モデル再パラメータ化**: YOLOv7は、グラデーション伝播経路の概念を持つ、さまざまなネットワークのレイヤーに適用可能な計画された再パラメータ化モデルを提案しています。

2. **動的ラベル割り当て**: 複数の出力層を持つモデルのトレーニングでは、異なるブランチの出力に動的なターゲットを割り当てる方法が新たな課題となります。この問題を解決するために、YOLOv7はコーストゥーファインリードガイド付きラベル割り当てと呼ばれる新しいラベル割り当て手法を導入しています。

3. **拡張スケーリングと複合スケーリング**: YOLOv7は、「拡張」および「複合スケーリング」の方法を提案し、効果的にパラメータと計算を利用できるリアルタイム物体検出器になります。

4. **効率性**: YOLOv7による方法は、最先端のリアルタイム物体検出器のパラメータ量を約40%、計算量を約50%効率的に削減し、より高速な推論速度と高い検出精度を実現します。

## 使用例

執筆時点では、Ultralyticsは現在、YOLOv7モデルをサポートしていません。そのため、YOLOv7を使用したい場合は、YOLOv7のGitHubリポジトリを直接参照する必要があります。

以下は、YOLOv7を使用するための典型的な手順の概要です。

1. YOLOv7のGitHubリポジトリにアクセスします: [https://github.com/WongKinYiu/yolov7](https://github.com/WongKinYiu/yolov7)。

2. READMEファイルに記載されている手順に従ってインストールします。通常、リポジトリをクローンし、必要な依存関係をインストールし、必要な環境変数を設定する必要があります。

3. インストールが完了したら、データセットの準備、モデルパラメータの設定、モデルのトレーニング、トレーニングされたモデルを使用して物体検出を実行するなど、リポジトリで提供されている使用方法に従って、モデルをトレーニングおよび使用することができます。

具体的な手順は、具体的なユースケースとYOLOv7リポジトリの現在の状態によって異なる場合があります。そのため、YOLOv7のGitHubリポジトリで提供されている手順を直接参照することを強くお勧めします。

YOLOv7のサポートが実装されるまで、このドキュメントを更新して、Ultralyticsの使用例を追加するための努力を続けます。

## 引用と謝辞

リアルタイム物体検出の分野での重要な貢献に対して、YOLOv7の著者に感謝いたします。

!!! Quote ""

    === "BibTeX"

        ```bibtex
        @article{wang2022yolov7,
          title={{YOLOv7}: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors},
          author={Wang, Chien-Yao and Bochkovskiy, Alexey and Liao, Hong-Yuan Mark},
          journal={arXiv preprint arXiv:2207.02696},
          year={2022}
        }
        ```

YOLOv7のオリジナル論文は[arXiv](https://arxiv.org/pdf/2207.02696.pdf)で見つけることができます。著者は自分たちの研究を広く公開しており、コードベースは[GitHub](https://github.com/WongKinYiu/yolov7)でアクセスできます。彼らの研究がこの分野を進め、他の研究者にもアクセス可能にする努力に感謝します。
