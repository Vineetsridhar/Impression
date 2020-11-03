import {StyleSheet} from 'react-native';

const styles = StyleSheet.create({
    container:{
        display:'flex',
        margin: 0,
	flexDirection: 'column',
	justifyContent: 'center',
	alignItems: 'center'
    },
    flexCode: {
	flex: 1
    },
    rowContainer: {
    	flex: 1,
	flexDirection: 'row',
	justifyContent: 'space-between'
    },
    schoolStyle: {
	textAlign: 'left',
	height: 50
    },
    emailStyle: {
	textAlign: 'right',
	height: 50
    },
})

export default styles
