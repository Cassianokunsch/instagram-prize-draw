# instagram-prize-draw

## Overview
Fala galera, tudo bom? Espero que sim! Estou compartilhando com vocês o meu Santo Graal, 
que é meu programa de comentar automagicamente os sorteios do Instagram, espero que seja
útil para vocês, porque pra mim vem sendo.

## Instalando
1. Você vai precisar instalar o Python 3.6 ou superior na sua máquina. Aqui o link https://www.python.org/downloads/
2. Instalar o Virtualenv (tem vários tutoriais na internet para diversos sistemas operacionais)
3. Dar um clone nesse repositório
4. Dar comando virtualenv env dentro da pasta do repositório clonado.
6. Dar o comando para ativar o virtualenv (Vária de Sistema Operacional)
5. Após ativar o virtualenv dentro do diretório "\instagram-prize-draw" dar o comando no seu terminal: pip install -r requirements.txt

## Como usar?

Para usar tem duas etapas:
### 1 Rodar o programa para extrair os seguidores e quem você segue

Nessa etapa os usuários são extraídos através do programa main_extract.py. Essa é uma etapa muito importante pois, é com 
ela que salvamos os usuários no banco de dados(não se preocupe é criado automagicamente) para serem usados na hora de fazer
os comentários.

Para extrair:
1. Rodar o comando python main_extract.py, se você estiver usando Virtualenv ative ele primeiro
2. Digitar o seu usuário do Instagram
3. Digitar a sua senha do Instagram
4. Informar se você quer extrair os seus seguidores ou quem você segue
5. Informar se você quer extrair novos, atualizar ou deletar
6. Aguardar o termino da extração

Obs.:
Passo 4 - O programa de extração te da a opção de você extrair os seus seguidores ou quem você segue. Eu recomendo você extrair o que você tem mais. Quanto mais seguidores ou quem você segue mais usuários você vai ter para comentar.

Passo 5 - A opção de extrair novos verifica se você seguiu alguém que não está no banco de dados ou se alguém novo
te seguiu que não está no banco de dados. A opção de atualizar atualiza todos os seguidores ou os usuários que você segue.
A opção de deletar marca como deletado os usuários que você deixou de seguir ou que vocẽ não segue mais.

### 2 Rodar o programa para comentar

Nessa etapa nos vamos rodar o programa main_auto_comment.py. Esse programa é o responsável por pegar os usuários extraídos e marcar eles no
sorteio que você escolher.

Para comentar:

1. Rodar o comando python main_auto_comment.py, se você estiver usando Virtualenv ative ele primeiro
2. Digitar seu usuário
3. Digitar o nome do perfil da promoção
4. Digitar o código da promoção
5. Digitar quantos amigos é para marcar por comentário
6. Escolher se você vai usar os seguidores ou quem você segue para marcar
7. Aguardar o termino do programa

Obs.:
Passo 5 - Para conseguir o código da promoção você deve entrar no Instagram pelo seu navegador, ir no perfil que está fazendo a promoção e no link do navegador pegar o nome entre / /, exemplo, para o link https://www.instagram.com/atleticafdv/?hl=pt-br o nome do perfil é atleticafdvs.

Passo 4 - Para conseguir o código da promoção você deve entrar no Instagram pelo seu navegador, ir no perfil que está fazendo a promoção, achar a foto oficial do sorteio e clicar nela, no link do navegador você deve pegar da URL apenas código entre /algum codigo/ depois do /p/, exemplo, para o link https://www.instagram.com/p/Bza8BHMhJAc/ o código é Bza8BHMhJAc.

## Informações importantes

### Programa de extração
1. Extrai um usuário a cada 1 segundo e meio para o Instagram não detectar que é spam.
2. A parte da extração pode ser feita apenas a primeira vez, mas é sempre bom deletar os usuários para não dar problema na hora de marcar pois ele pode ter te bloqueado e isso vai atrapalhar o programa.
3. Geramente quando se tem muitos usuários pode demorar um pouco para extrair e talvez até o Instagram falar que é Spam, mas é só aguardar um dia e rodar o programa de novo para extrair. Você também pode cancelar o programa que se você rodar de novo ele vai continuar de onde parou.

### Programa de comentar
1. Salva em uma pasta, chamada Madecomments, os comentários feitos. Então você pode parar o programa quando quiser que ele vai filtrar os ultimos marcados e vai marcar só quem ainda foi não marcado. Se vocẽ marcou todo mundo e quer marcar tudo de novo é só excluir o arquivo que ele vai marcar tudo de novo. O arquivo é criado nesse padrão perfildapromocao_codigosorteio_usuario.txt, exemplo, atleticafdv_Bza8BHMhJAc_cassianokunsch.txt
2. Faz um comentário entre 10 a 120 segundos, para o Instagram não bloquear como spam. Cada conta tem limite de comentário, varia muito, se na hora que o programa estiver rodadando aparecer a mensagem "Spam detectado" aguarde pelo menos um dia.
para rodar o programa de novo para dar tempo de "desbloquearem sua conta".
3. Tem uma lógica em relação a escolher os usuários para marcar nos sorteios. Vários sorteios
não querem que você marque faker ou pessoas famosas, então na hora de criar a lista de usuários filtrando 
apenas os usuários que respeitarem a lógica desse trecho de código abaixo. Você pode mudar se quiser.

```
def select_filter_comment(self, table, user_id):
        result = self.session.query(table).filter(table.users_id == user_id,
                                                  table.delete == '',
                                                  table.following_count > 500,
                                                  table.following_count < 3000,
                                                  table.follower_count > 500,
                                                  table.follower_count < 4000).all()
```


## Considerações finais

Bom galera é isso, se ficou alguma dúvida pode me mandar no meu e-mail(cassiano.kunsch@outlook.com). Eu fiz esse programa por diversão se vocês quiserem melhorar é so fazer um fork do projeto e fazer um pull request, se eu achar legal vou fazer o merge. Caso dê algum problema é só abrir uma issue. Espero que tenha ficado claro todo o processo. Mais uma coisa, não usem o programa nos mesmos sorteios que eu haha.
