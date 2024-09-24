
# Pergunta:
### Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser.
Seu objetivo é descobrir qual interruptor controla qual lâmpada.
Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  

# Desafio das lampadas
Para resolver esse problema usando apenas duas idas até uma das salas das lâmpadas, você pode usar o calor da lâmpada como uma pista adicional. A estratégia é a seguinte:

1. **Primeiro Passo (na sala com os interruptores):**
   - Ligue o **primeiro interruptor** e deixe-o ligado por alguns minutos.
   - Após esse tempo, desligue o **primeiro interruptor** e ligue o **segundo interruptor**.
   - Deixe o **terceiro interruptor** desligado.

2. **Primeira Ida à sala das lâmpadas:**
    - Vá até a sala das lâmpadas e observe o estado das lâmpadas.
    - A lâmpada que está **acesa** é controlada pelo **segundo interruptor** (pois está ligado agora).
    - A lâmpada que está **apagada, mas quente** é controlada pelo **primeiro interruptor** (pois esteve ligada por um tempo e acabou de ser desligada).
    - A lâmpada que está **apagada e fria** é controlada pelo **terceiro interruptor** (que nunca foi ligado).

Com isso, você consegue determinar qual interruptor controla cada lâmpada com apenas uma ida até a sala das lâmpadas.
