import streamlit as st
import pandas as pd
import joblib

# 1. تحميل الموديل المعالج
@st.cache_resource 
def load_model():
    return joblib.load('churn_prediction_pipeline.pkl')

model = load_model()

# 2. إعدادات واجهة المستخدم بلمسة احترافية
st.set_page_config(page_title="كاشف التسرب", page_icon="📊", layout="centered")
st.title("📊 نظام التنبؤ الذكي بمغادرة العملاء")
st.write("بناءً على تحليل البيانات، هندخل مواصفات العميل هنا والسيستم هيقولنا بوضوح هل العميل ده مكمل معانا ولا محتاجين نلحقه قبل ما يمشي.")
st.markdown("---")

# 3. واجهة إدخال البيانات المنطقية
col1, col2 = st.columns(2)

with col1:
    st.subheader("البيانات الديموغرافية والمالية")
    age = st.number_input("عمر العميل الحالي:", min_value=18, max_value=100, value=30)
    tenure = st.number_input("مدة الارتباط بالشركة (شهور):", min_value=1, max_value=100, value=12)
    charges = st.number_input("متوسط الدفع الشهري ($):", min_value=10.0, max_value=200.0, value=50.0)

with col2:
    st.subheader("تفاصيل التعاقد والدعم")
    contract = st.selectbox("نوع التعاقد الحالي:", ['Month-to-month', 'One year', 'Two year'])
    tech_support = st.selectbox("هل مشترك في الدعم الفني؟", ['Yes', 'No'])

st.markdown("---")

# 4. معالجة البيانات وإظهار النتيجة بمنطق محلل بيانات
if st.button("تحليل حالة العميل الآن 🔍", use_container_width=True):
    
    # تجهيز البيانات للنموذج
    input_data = pd.DataFrame({
        'Age': [age],
        'Tenure_Months': [tenure],
        'Monthly_Charges': [charges],
        'Contract_Type': [contract],
        'Tech_Support': [tech_support]
    })
    
    # التوقع باستخدام الـ Pipeline
    prediction = model.predict(input_data)[0]
    
    # عرض النتائج النهائية
    if prediction == 1:
        st.error("⚠️ إنذار: العميل ده في مرحلة 'خطر عالٍ' ومستعد لإلغاء الاشتراك في أي لحظة.")
        st.info("💡 إجراء مقترح: العميل ده محتاج تدخل فوري، فكر في تقديم عرض خصم أو نقله لعقد سنوي لزيادة ولائه.")
    else:
        st.success("✅ حالة مستقرة: المؤشرات بتقول إن العميل راضي عن الخدمة ومكمل معانا بنسبة كبيرة.")
        st.balloons()