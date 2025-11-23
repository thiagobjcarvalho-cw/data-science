#!/bin/bash
# Script de Execução Automatizada - Prova AEDI UnB
# Executa todos os notebooks e gera HTMLs para entrega

set -e  # Parar em caso de erro

echo "========================================="
echo "  PROVA FINAL AEDI - UnB PPCA"
echo "  Execução Automatizada"
echo "========================================="
echo ""

# Cores
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Diretórios
NOTEBOOKS_DIR="prova-aedi-unb/notebooks"
EXPORTS_DIR="prova-aedi-unb/exports"

# Criar pasta de exports
echo -e "${YELLOW}📁 Criando diretório de exports...${NC}"
mkdir -p "$EXPORTS_DIR"

# Notebooks a executar
NOTEBOOKS=("Q1_Regressao_Linear" "Q2_Regressao_Logistica" "Q3_ANOVA" "Q4_ML_Avancado")
TOTAL=${#NOTEBOOKS[@]}
COUNT=0

echo -e "${GREEN}✅ Diretório criado!${NC}"
echo ""

# Executar cada notebook
for notebook in "${NOTEBOOKS[@]}"; do
    COUNT=$((COUNT + 1))
    echo "========================================="
    echo -e "${YELLOW}[$COUNT/$TOTAL] Executando: ${notebook}.ipynb${NC}"
    echo "========================================="

    START=$(date +%s)

    # Executar e converter para HTML
    if jupyter nbconvert \
        --to html \
        --execute \
        --ExecutePreprocessor.timeout=1800 \
        --no-input \
        "$NOTEBOOKS_DIR/${notebook}.ipynb" \
        --output "$EXPORTS_DIR/${notebook}.html"; then

        END=$(date +%s)
        DURATION=$((END - START))

        echo -e "${GREEN}✅ ${notebook} concluído em ${DURATION}s!${NC}"
        echo ""
    else
        echo -e "${RED}❌ ERRO ao executar ${notebook}${NC}"
        echo ""
        exit 1
    fi
done

echo "========================================="
echo -e "${GREEN}🎉 TODOS OS NOTEBOOKS EXECUTADOS!${NC}"
echo "========================================="
echo ""

# Listar HTMLs gerados
echo "📊 HTMLs gerados em $EXPORTS_DIR:"
ls -lh "$EXPORTS_DIR"/*.html 2>/dev/null || echo "Nenhum HTML encontrado"

echo ""
echo "========================================="
echo -e "${GREEN}✅ PROVA COMPLETA - Pronta para entrega!${NC}"
echo "========================================="
echo ""
echo "📤 Próximos passos:"
echo "  1. Verifique os HTMLs em: $EXPORTS_DIR/"
echo "  2. Abra cada HTML no navegador para revisar"
echo "  3. Envie os 4 HTMLs para o Moodle"
echo ""
