#!/usr/bin/env bash
# Encerra o script se qualquer comando falhar
set -o errexit

echo "🔧 Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

echo "📦 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "🗃️ Aplicando migrações no banco de dados..."
python manage.py migrate

echo "✅ Build concluído com sucesso!"
