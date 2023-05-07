# A collection of talks, code kata, experiments and other expercises 

## Talks - Nosetools
Location: [talk-nosetools](talk-nosetools).

A few bullet points to aid a talk on test-driven development in Python 2 with Nosetools. It contains just a few basics
and some caveats about the testing framework, mocking and monkey-patching in Python.

## Helm
Location: [helm](helm).

Some experiments in Helm and values and general templating.

Setting things up: `helm create mychart` 

Cascading of custom values in Helm. Expecially important in my case was `.\outsideDeeperValues.yaml` which because it's
outside the chart requires and anchor and is represented at different depths in the same value-file.

```pwsh
cd mychart
helm package mychart
helm template mychart -f .\config\development.yaml | Select-String -Pattern "env:" -Context 5
```

