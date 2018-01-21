import Vue from 'vue'

import VueFire from 'vuefire'
import Firebase from 'firebase'

Vue.use(VueFire)

var config = {
  apiKey: 'AIzaSyC-EVIfBW1AutzPb-bXOS3r_xBdcMDWQbk',
  authDomain: 'redhat-vuejs-project.firebaseapp.com',
  databaseURL: 'https://redhat-vuejs-project.firebaseio.com',
  projectId: 'redhat-vuejs-project',
  storageBucket: 'redhat-vuejs-project.appspot.com',
  messagingSenderId: '522205275247'
}

let app = Firebase.initializeApp(config)
export const db = app.database()
