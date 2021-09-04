# Baixando e iniciando o script

> Faça o download do repositório
```
git clone https://github.com/reiscaslureis/text-files-to-pdf.git
```

> Entre na pasta
```
cd text-files-to-pdf
```

> Instale as dependências
```
pip install -r requirements.txt
```

> Inicie o script
- Windows
```
python main.py
```

- Linux
```
python3 main.py
```

# Comandos
- ### d 'directory'
Representa o diretório onde todos os arquivos de texto estão, se necessário, crie uma pasta para todos os arquivos

- ### s 'x' 'y'
Após ter selecionado o diretório, todos os arquivos nele aparecerão no terminal com um índice, a ordem que aparece é a ordem que o pdf vai ser gerado. Você pode modificar isso com o comando swap, passando como argumento os dois índices dos arquivos de texto que serão trocados de lugar

- ### i 'x' 'y'
Comando para inserir um arquivo de índice 'x' no índice 'y', fazendo com que o antigo arquivo que ocupava o lugar desça um índice. Diferente do comando s, ele não faz a troca dos arquivos

- ### o 'output-name'
Este comando representa o nome do arquivo final, por padrão é 'result'

- ### l
Caso tenha alguma mudança nos arquivos dentro do diretório selecionado, o script precisa ser atualizado para que os novos arquivos sejam adicionados ou os antigos sejam removidos, para isso, usa-se o comando load

Obs: O load reseta todas as configurações do swap

- ### r
Para gerar o pdf final, utilize o comando run

Obs: O pdf será gerado no mesmo diretório que o arquivo 'main.py' se encontra

- ### q
Finaliza o script
