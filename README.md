# Fundamentos de Computação Tooltorial

Neste tutorial faremos uma aplicação simples em Python para validar conceitos básicos na linguagem Python e versionamento de código. Essa aplicação vai validar se um URL está online ou offline e retornar uma mensagem para o usuário.

A estrutura do projeto será:

```
README.md
requirements.txt
site_checker.sh
setup.py
sitechecker/
├── checker.py
├── __init__.py
├── __main__.py
```
# Instruções

## 1. Criar o ambiente de trabalho

Para criar um projeto python é recomendável trabalhar com ambientes virtuais, para isso você iniciar um terminal e rodar os seguintes comandos:

- Baixe o repositório em sua máquina, ou clone no terminal com o comando:
```
git clone https://github.com/Lineker98/desafio-indicium.git
cd desafio-indicium/
```

- Criação do ambiente virtual para instalação das dependências:
```
pip install virtualenv
```

- Com o venv instalado, e dentro do diretório do projeto, execute:
```
python3 -m venv <nome_do_ambiente>
```

- Para ativação do ambiente, digite no terminal
    - Linux:
    ```console
    source <nome_do_ambiente>/bin/activate
    ```

    - Windows:
    ```
    <name_do_ambientet>\Scripts\activate
    ```

- Com o ambiente já instalado e ativado, precisamos agora instalar as dependências, ainda no terminal, digite:

```
pip install -r requirements.txt
```


## 2. Executar a aplicação

 - Para veirificar as opções de argumentos via terminal, digite:
 ```
 python -m sitechecker --help
 ```

 Assim você pode criar um arquivo txt com todas as urls que deseja consultar e passar seu caminho
 para o parâmetro "-f".

 Além disso, podemos passar as urls diretamente via terminal, digitando "--urls" para cada url desejada. Exemplo:
 ``` 
 python -m sitechecker --urls globo.com --urls google.com --urls globoesporte.com
 ```

 Caso deseja verificar muitos websites, podemos utilizar o parâmetro de multiprocessamento.
 ```
 python -m sitechecker -f urls.txt --multiprocessing
 ```

## 3 Instalar a aplicação (Opcional)

 - Para Instalar a aplicação basta digitar:
 ```
 pip install -e . 
 ```

 Agora você pode utilizar o comando "sitechecker diretamente do terminal":
 ```
 sitechecker -f urls.txt --multiprocessing
 ```

# Credits

Exemplo baseado em:
https://realpython.com/site-connectivity-checker-python/