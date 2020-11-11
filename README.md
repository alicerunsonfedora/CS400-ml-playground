<img src="tc.png" align="right"/>

# CostumemasterML

**CostumemasterML (Codename Teal Converse)** is an artificial intelligence agent strategy for the game [_The Costumemaster_][game], a puzzle game about costume-switching. CostumemasterML uses a machine learning decision tree model trained with CoreML to generate its next best actions based on state assessments.

This repository contains the materials needed to generate a model using Create ML that can be imported into the source code for The Costumemaster (or in the app's resources).

## Table of Contents

- [Why use CoreML?](#Why-separate-this-and-use-CoreML)
- [How does this work?](#How-is-this-possible)
- [Usage](#Usage)
  - [Requirements](#Requirements)
  - [Getting started](#Getting-started)
  - [Creating a model source](#Creating-a-model-source)
    - [Provide testing data](#Provide-testing-data)
  - [Train and export the model](#Train-and-export-the-model)
    - [Creating random data](#Creating-random-data)
- [Caveats](#Caveats)

## Why separate this and use CoreML?

While it is possible to make a decision tree using `GKDecisionTree` for the game, there are some complications:

- Depending on how many attributes you are assessing in the tree, the height of this tree will grow.
- Making a decision with the decision tree also requires a set of examples.
  - If you provide too little, you will encounter dimension errors.
  - If you provide enough, you _should_ be able to generate a tree just fine. However, in my case and on my device, I constantly ran up a wall and ended up getting back a nasty `EXC_BAD_ACCESS` error due to issues surrounding GKDecisionTree's CART growth algorithm.

Thankfully, Apple provides some ML tools that can be used in place of the decision tree in the game. Provided that we create an ML model, we should be able to run basic classification/regression operations so that the game can make a proper decision.

## How is this possible?

The decision tree agents break up the game world into a series of questions, which can be described as "features" for a given state. Provided that we convert these live assessments into raw data that Create ML can parse such as CSV or JSON, Create ML can generate a decision tree model for us using some ML magic. This model can then be imported into the game for future AI use.

## Usage

### Requirements

- A Mac running macOS 10.15 Catalina or greater
- Xcode 12 or greater

### Getting started
To get started, clone the repository and open the TealConverse.mlproj file in Create ML. Some model sources are provided already that can be exported into the main game.

### Creating a model source
Create a new model source by clicking the plus icon next to "Model Sources". In the Settings tab, click on "Choose" in the training data section to provide a CSV file that represents the training state data to use. The training data file should have the exact same names as the state assessments in the main game.

You'll also need to configure the following settings:

- **Target**: action
- **Features**: Select all of the attributes except for action in the list.
- **Algorithm**: Decision Tree
- **Max Depth**: 16 (adjust this as necessary)
- **Min. Loss Reduction**: 0 (adjust this as necessary)
- **Min Child Weight**: 0.1 (adjust this as necessary)

#### Provide testing data

By default, the model source will take a chunk of the training data and use that chunk for testing purposes. In most cases, this is acceptable. If you want to change to your own testing data (such as data created from the random data generator), follow the same steps as the training data selection for your testing data set.

### Train and export the model
When you're ready to train the model, click "Train" in the toolbar. You can then go to the Output tab and click "Get" to save the file to the disk. This model file can be imported into Xcode by dragging the file into the **Conscious/Assets/Models** group in the navigator.

> :warning: Make sure that the exported file name is `TealConverse.mlmodel` before importing into Xcode. Naming it differently will require source code changes to the `AITealConverseStrategist` in the main game.

### Creating random data

To create a CSV file with random state data, a Python script `generate_random.py` is provided with the repository.

In a terminal, run `generate_random.py`. You can supply an additional argument, `--amount`, and specify how many entries you want in the data set. By default, the script will generate a file with 50 entries.

## Caveats

Although using this method of generating decisions works a lot more reliably than using GameplayKit's learned decision trees, there are a couple of major caveats to using this method.

- **The data is essentially predetermined.** The agent will be making decisions based on what the model states. Since this model is generated ahead of time, it has to rely on history someone else provides.
- **Using this model may cause issues.** If the model is unable to predict a value or something is corrupt with the model file, the default action is used, which is not optimal.
- **This model cannot be updated in-game.** The agent will not be able to use previous actions to teach itself the rules.
- **The model is oblivious to the real game state.** The model is unaware of what inputs exist, where the exit is, etc. The model is designed for general decision-making that is agnostic to the level it's playing.

<!-- Links -->
[game]: https://costumemaster.marquiskurt.net