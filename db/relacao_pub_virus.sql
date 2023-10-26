-- Active: 1697837181008@@localhost@5432@postgres@public
/* ---------------------------------------------
Esquema de relações - Publicação virus

Jornal (Sigla_Jornal(PK), nome_jornal, volume, edicao)
Publicacao (Cod_pub(PK), titulo, resumo, dt_publi,sigla_jornal (FK)NN ) 

Publ_interna(Cod_publ_interna(PK)(FK),Num_contrato(FK)NN)

Cod_publ_interna referencia Publicacao
Num_Contrato referencia Contrato

Contrato (Num_contrato(PK), vl_financiado, dt_ini_contrato, dt_termino_contrato)
Autor (cod_autor(PK), nome_autor, pais_autor, especialidade, sexo_autor)
Instituicao (sigla_inst(PK), nome_inst, tipo_inst, pais_inst, end_inst)
Autoria (Cod_publ(PK)(FK), sigla_inst(PK)(FK))
Virus (sigla_virus(PK)(FK),cod_autor(PK)(FK),sigla_inst(PK)(FK))
Publ_virus (Cod_publ(PK)(FK),sigla_virus(PK)(FK))
Publ_referencias (Cod_publ(PK)(FK),Cod_publ_referenciada(PK)(FK))

----------------------------------------------- */
-- Active: 1697837181008@@localhost@5432@postgres@public
/* ---------------------------------------------
Esquema de relações - Publicação virus

Jornal (Sigla_Jornal(PK), nome_jornal, volume, edicao)
Publicacao (Cod_pub(PK), titulo, resumo, dt_publi,sigla_jornal (FK)NN ) 

Publ_interna(Cod_publ_interna(PK)(FK),Num_contrato(FK)NN)

Cod_publ_interna referencia Publicacao
Num_Contrato referencia Contrato

Contrato (Num_contrato(PK), vl_financiado, dt_ini_contrato, dt_termino_contrato)
Autor (cod_autor(PK), nome_autor, pais_autor, especialidade, sexo_autor)
Instituicao (sigla_inst(PK), nome_inst, tipo_inst, pais_inst, end_inst)
Autoria (Cod_publ(PK)(FK), sigla_inst(PK)(FK))
Virus (sigla_virus(PK)(FK),cod_autor(PK)(FK),sigla_inst(PK)(FK))
Publ_virus (Cod_publ(PK)(FK),sigla_virus(PK)(FK))
Publ_referencias (Cod_publ(PK)(FK),Cod_publ_referenciada(PK)(FK))

----------------------------------------------- */

-- Cria o BD caso não exista
SELECT 'CREATE DATABASE pubcientifica' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'pubcientifica')
