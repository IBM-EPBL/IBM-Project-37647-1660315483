{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "private_outputs": true,
      "provenance": [],
      "authorship_tag": "ABX9TyMQ3ZLlL17rYUMMdX5N9oNU",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/IBM-EPBL/IBM-Project-37647-1660315483/blob/main/Final%20Deliverables/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "0Ft8PJMG4E-N"
      },
      "outputs": [],
      "source": [
        "from flask import Flask, render_template, request\n",
        "import pickle\n",
        "app=Flask(__name__ ,template_folder='template')\n",
        "\n",
        "@app.route('/')\n",
        "def home():\n",
        "    return render_template('home.html')\n",
        "\n",
        "@app.route('/index')\n",
        "def index():\n",
        "    return render_template('index.html')\n",
        "\n",
        "@app.route('/data_predict',methods=['POST'])\n",
        "def data_predict():\n",
        "    age=request.form['Age']\n",
        "    gender=request.form['Gender']\n",
        "    tb=request.form['Total_Bilirubin']\n",
        "    db=request.form['Direct_Bilirubin']\n",
        "    ap=request.form['Alkaline_Phosphotase']\n",
        "    aa1=request.form['Alamine_Aminotransferase']\n",
        "    aa2=request.form['Aspartate_Aminotransferase']\n",
        "    tp=request.form['Total_Protiens']\n",
        "    a=request.form['Albumin']\n",
        "    agr=request.form['Albumin_and_Globulin_Ratio']\n",
        "\n",
        "    data=[[float(age),float(gender),float(tb),float(db),float(ap),float(aa1),float(aa2),float(tp),float(a),float(agr)]]\n",
        "\n",
        "    model=pickle.load(open('liver_analysis.pkl','rb'))\n",
        "    prediction=model.predict(data)[0]\n",
        "\n",
        "    if prediction==1:\n",
        "        return render_template(\"Chance.html\")\n",
        "    else:\n",
        "        return render_template(\"noChance.html\")\n",
        "    \n",
        "\n",
        "\n",
        "\n",
        "if __name__=='__main__':\n",
        "    app.debug=True\n",
        "    app.run(host='0.0.0.0',port=5000)"
      ]
    }
  ]
}