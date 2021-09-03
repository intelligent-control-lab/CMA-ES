# CMA-ES

A CMA-ES implementation. 

To use CMA-ES, define an evaluator in evaluator.py following `test_evaluator`, and create a learning config file following  `test_config.yaml`. The following command runs CMA-ES to minimize a quadratic equation.

```bash
python cma-es.py test_config.yaml
```

We also give another example: tuning parameters of a PD controller by CMA-ES.

```bash
python cma-es.py pd_config.yaml
```

Tried parameters and rewards are stored in `logs`.