# view_intern

O que fiz nesse passo:
- criei um arquivo chamado main.py
- criei um módulo chamado "módulo_teste"
- criei um arquivo dentro do módulo chamado "__init__.py"
- inseri o código de print no "__init__.py" com uma função chamada "imprimindo_algo"

```bash
mkdir module_teste
echo -e "from module_teste import imprimindo_algo \n\nprint(imprimindo_algo())" >> main.py
echo -e "# -*- coding: utf-8 -*- \n\ndef imprimindo_algo():\n    return 'Olá comendador!'" >> module_teste/__init__.py
git add .
git commit -m"inserindo a função de print do comendador"
git push origin master
```