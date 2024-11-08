import pandas as pd
import plotly.express as px
import streamlit as st
st.set_page_config(
    page_title='Analytics Portal',
    page_icon='📊'
    )

#title
st.title(':rainbow[Data Analytics Portal]')
st.header(':grey[Transformed Data]')
file=st.file_uploader('Drop csv or excel file' ,type=['csv','xlsx'])
if (file!=None):
    if(file.name.endswith('csv')):
        data=pd.read_csv(file)
    else:
        data=pd.read_excel(file)
    st.dataframe(data)
    st.info('File uploaded successfully')
    st.subheader(':rainbow[Basic infomation of the dataset]',divider='rainbow')
    tab1,tab2,tab3,tab4=st.tabs(['Summary','Top and Bottom Rows','Datatype','columns'])
    with tab1:
        st.write(f'There are{data.shape[0]} rows in dataset and {data.shape[1]} columns in the dataset')
        st.subheader(':grey[Statistical Summary]')
        st.dataframe(data.describe())
    with tab2:
        st.subheader(':grey[Top Rows]')
        topRows=st.slider('numbers of rows you want ',1,data.shape[0],key='topslider')
        st.dataframe(data.head(topRows))
        st.subheader(':grey[Bottom Rows]')
        bottmRows=st.slider('numbers of rows you want ',1,data.shape[0],key='bottomslider')
        st.dataframe(data.tail(bottmRows))
    with tab3:
        st.subheader(':grey[Data types of columns]')
        st.dataframe(data.dtypes)
    with tab4:
        st.subheader(':grey[column name in dataset]')
        st.dataframe(list(data.columns))
    st.subheader(':rainbow[column values to count]',divider='rainbow')
    with st.expander('Value Count'):
        col1,col2=st.columns(2)
        with col1:
             column=st.selectbox('Choose column name',options=list(data.columns))
        with col2:
             topRows=st.number_input('Top rows',min_value=1,step=1)
        count=st.button('count')
        if (count==True):
            result=data[column].value_counts().reset_index().head(topRows)
            st.dataframe(result)
#visualization
            st.subheader('Visualization',divider='gray')
            fig=px.bar(data_frame=result,x=column,y='count',template='plotly_white')
            st.plotly_chart(fig)
            fig=px.line(data_frame=result,x=column,y='count',template='plotly_white')
            st.plotly_chart(fig)
            fig=px.pie(data_frame=result,names=column,values='count',template='plotly_white')
            st.plotly_chart(fig)
            fig=px.sunburst(data_frame=result,names=column,values='count',template='plotly_white')
            st.plotly_chart(fig)
    
    st.subheader('Group by Analysis')
    with st.expander('Group by columns'):
        col1, col2, col3 = st.columns(3)
        with col1:
            groupby_cols = st.multiselect('choose your column', options=list(data.columns))
        with col2:
            operation_col = st.selectbox('choose column for operation', options=list(data.columns))
        with col3:
            operation = st.selectbox('choose operation', options=['max', 'min', 'sum', 'mean', 'median', 'count'])
        
        if groupby_cols:
            # Convert mixed data types to a common type (e.g., string)
            data[operation_col] = data[operation_col].astype(str)
            
            result = data.groupby(groupby_cols).agg(
                newcol=(operation_col, operation)
            ).reset_index()
            
            st.dataframe(result)


            
            st.subheader(':grey[Data Visualization]',divider='gray')
            graphs=st.selectbox('choose your graphs',options=['line','bar','scatter','pie','histogram','box'])
            if (graphs=='line'):
                x_axis=st.selectbox('choose x axis',options=list(result.columns))
                y_axis=st.selectbox('choose y axis',options=list(result.columns))
                color=st.selectbox('color information',options=[None]+list(result.columns))
                fig=px.line(data_frame=result,x=x_axis,y=y_axis,color=color,markers=True)
                st.plotly_chart(fig)
            elif (graphs=='bar'):
                x_axis=st.selectbox('choose x axis',options=list(result.columns))
                y_axis=st.selectbox('choose y axis',options=list(result.columns))
                color=st.selectbox('color information',options=[None]+list(result.columns))
                facet_col=st.selectbox('column information',options=[None]+list(result.columns))
                fig=px.bar(data_frame=result,x=x_axis,y=y_axis,color=color,facet_col=facet_col)
                st.plotly_chart(fig)
            elif (graphs=='scatter'):
                  x_axis=st.selectbox('choose x axis',options=list(result.columns))
                  y_axis=st.selectbox('choose y axis',options=list(result.columns))
                  color=st.selectbox('color information',options=[None]+list(result.columns))
                  size=st.selectbox('size information',options=[None]+list(result.columns))
                  fig=px.scatter(data_frame=result,x=x_axis,y=y_axis,color=color,size=size)
                  st.plotly_chart(fig)
            elif graphs == 'pie':
                values = st.selectbox('choose numerical values', options=list(result.columns)) 
                names = st.selectbox('choose labels', options=list(result.columns)) 
                fig = px.pie(data_frame=result, values=values, names=names) 
                st.plotly_chart(fig)
            
            elif graphs == 'histogram':
                x_axis = st.selectbox('choose x axis', options=list(result.columns))
                color = st.selectbox('color information', options=[None] + list(result.columns))
                fig = px.histogram(data_frame=result, x=x_axis, color=color)
                st.plotly_chart(fig)
            elif graphs == 'box':
                x_axis = st.selectbox('choose x axis', options=list(result.columns))
                y_axis = st.selectbox('choose y axis', options=list(result.columns))
                color = st.selectbox('color information', options=[None] + list(result.columns))
                fig = px.box(data_frame=result, x=x_axis, y=y_axis, color=color)
                st.plotly_chart(fig)
                
    
                
                
            
            
            
            





