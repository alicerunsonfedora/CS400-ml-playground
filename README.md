# CostumemasterML
**_Codename Yellow Converse_**

The following repository contains the CoreML/Create ML materials to make a decision tree learning model for AI agents in [The Costumemaster][game], a puzzle game about costume-switching.

## Why separate this and use CoreML?

While it is possible to make a decision tree using `GKDecisionTree` for the game, there are some complications:

- Depending on how many attributes you are assessing in the tree, the height of this tree will grow.
- Making a decision with the decision tree also requires a set of examples.
  - If you provide too little, you will encounter dimension errors.
  - If you provide enough, you _should_ be able to generate a tree just fine. However, in my case and on my device, I constantly ran up a wall and ended up getting back a nasty `EXC_BAD_ACCESS` error due to issues surrounding GKDecisionTree's CART growth algorithm.

Thankfully, Apple provides some ML tools that can be used in place of the decision tree in the game. Provided that we create an ML model, we should be able to run basic classification/regression operations so that the game can make a proper decision.

## How is this possible?

The decision tree agents break up the game world into a series of questions, which can be described as "features" for a given state. Provided that we convert these live assessments into raw data that Create ML can parse such as CSV or JSON, Create ML can generate a decision tree model for us using some ML magic. This model can then be imported into the game for future AI use.

<!-- Links -->
[game]: https://costumemaster.marquiskurt.net