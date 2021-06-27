import streamlit as st


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)


class stNotification:
    """
    This is the custom notification
    """
    def build_style(self):
        "Getting theme colors"
        pc = st.get_option('theme.primaryColor')
        bc = st.get_option('theme.backgroundColor')
        sbc = st.get_option('theme.secondaryBackgroundColor')
        tc = st.get_option('theme.textColor')
        return {'pc': pc, "bc": bc, "sbc": sbc, "tc": tc}

    def __init__(self, text="lorem", spinner=True):
        "Getting default theme and building style"
        styles = self.build_style()

        "Spinner"
        if spinner:
            loader = f'<div ><div class = "loader" style ="line-height: 2rem;text-align: center;border-left: 0.3em solid {styles["pc"]};" ></div></div>'
        else:
            loader = '<br>'
#            <div class="custom-notification" style="font-size:0.8rem;min-width:40%;max-width:62%;top:0rem;background-color: #0E1117;border-bottom-right-radius: 9px;border-bottom-left-radius: 9px;padding: 0.5rem;position: fixed;line-height: 2rem;text-align: center;border-left: 2px solid {styles['pc']};border-right: 2px solid {styles['pc']};border-bottom: 2px solid {styles['pc']}">

        "Building notification object"
        self.notification = f'''
            <div class="custom-notification" style="font-size:0.8rem;min-width:40%;max-width:62%;top:0rem;background-color: {styles["bc"]};padding: 0.5rem;position: fixed;line-height: 2rem;text-align: center;border-style: solid;border-width: 2px;border-image: linear-gradient(-90deg,{styles['bc']}, {styles['pc']}) 1;border-top-width:0px;border-right-width:0px;">
                <div style="display: flex;flex-wrap: nowrap;">
                    {loader}
                    <div style="margin-left:1rem;">
                        {text}
                    </div>
                </div>
            </div>
            '''

    def __enter__(self):
        self.notification_object = st.markdown(
            self.notification, unsafe_allow_html=True)

    def __exit__(self, *args, **kwargs):
        self.notification_object.empty()
        
        
def set_page_title(title):
    """
    This function sets the app title, and removes the • Streamlit
    """
    st.sidebar.markdown(unsafe_allow_html=True, body=f"""
        <iframe height=0 srcdoc="<script>
            const title = window.parent.document.querySelector('title') \
                
            const oldObserver = window.parent.titleObserver
            if (oldObserver) {{
                oldObserver.disconnect()
            }} \

            const newObserver = new MutationObserver(function(mutations) {{
                const target = mutations[0].target
                if (target.text !== '{title}') {{
                    target.text = '{title}'
                }}
            }}) \

            newObserver.observe(title, {{ childList: true }})
            window.parent.titleObserver = newObserver \

            title.text = '{title}'
        </script>" />
    """)