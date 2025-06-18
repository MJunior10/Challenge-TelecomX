# Análise de Churn de Clientes

Este relatório apresenta uma análise visual de um conjunto de dados relacionados ao **churn** (cancelamento de serviço) de clientes de uma empresa de telecomunicações. Os gráficos abaixo foram gerados para identificar padrões e relações entre variáveis como idade, tipo de serviço de internet e tempo de permanência (tenure) com o churn.

---

## 1. Distribuição de Idosos



Este gráfico de pizza representa a proporção de clientes idosos na base de dados. Observa-se que:

- **83,7%** dos clientes **não são idosos**.
- Apenas **16,3%** são **idosos**.

Essa distribuição mostra que a maioria da base de clientes é composta por pessoas abaixo de 65 anos. Essa informação pode ser útil para segmentar ações de marketing e personalização de ofertas.

---

## 2. Churn por Tipo de Internet



Este gráfico de barras agrupa o churn de clientes com base no tipo de serviço de internet contratado:

- Clientes com **DSL** têm uma taxa menor de churn.
- Clientes com **Fibra Óptica** apresentam **maior incidência de churn**.
- Clientes **sem serviço de internet** têm uma taxa de churn muito baixa.

Esse resultado indica que clientes de fibra óptica são mais propensos a cancelar o serviço, o que pode apontar para problemas de preço, qualidade ou atendimento.

---

## 3. Distribuição de Tenure por Churn



O gráfico de caixa (boxplot) mostra a distribuição do tempo de permanência dos clientes (tenure) em meses, separados por churn:

- Clientes que **não cancelaram** têm, em média, **tenure maior**.
- Clientes que **cancelaram** o serviço tendem a sair nos **primeiros meses** de contrato.

Esse comportamento reforça a importância do engajamento e da satisfação nos primeiros meses após a aquisição do serviço.

---

## 4. Tenure vs Churn (Boxplot Alternativo)



Este boxplot complementa a análise anterior, reforçando a tendência de **menor tempo de permanência** para clientes que cancelaram. A mediana dos que permanecem é visivelmente superior. O gráfico também mostra que há clientes fiéis com até 72 meses de permanência, indicando a possibilidade de fidelização.

---

## Conclusão

Os gráficos sugerem que:

- Idosos não são o público majoritário, mas seu comportamento pode merecer análise específica.
- O tipo de internet influencia o churn, especialmente entre usuários de fibra óptica.
- O tempo de permanência é um indicador claro de risco de churn — clientes que permanecem pouco tempo tendem a cancelar mais.
  
Essas análises podem orientar ações preventivas, como melhorias no serviço de fibra óptica, programas de fidelização nos primeiros meses e segmentação por faixa etária.



