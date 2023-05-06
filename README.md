# A collection of talks, code kata, experiments and other expercises 

## Talks - Nosetools
Location: [talk-nosetools](talk-nosetools).

A few bullet points to aid a talk on test-driven development in Python 2 with Nosetools. It contains just a few basics
and some caveats about the testing framework, mocking and monkey-patching in Python.

## Helm
Location: [helm](helm).

Some experiments in Helm and values and general templating.

Setting things up: `helm create mychart` 

Cascading of custom values in Helm

```pwsh
helm package mychart
helm template .\mychart-0.1.0.tgz -f .\myvalues.yaml > deployment-example.yaml
cat deployment-example.yaml | Select-String -Pattern customValue -Context 1
#             value: "Below should be a custom value"
# >           name: customValue
#             securityContext:
```

