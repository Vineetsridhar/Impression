import { StyleSheet } from 'react-native';
import colors from '../../config/colors';
import font from '../../config/font'
const styles = StyleSheet.create({
    container: {
        display: 'flex',
        margin: 0,
        flexDirection: 'column',
        backgroundColor: colors.background,
        flex: 1
    },
    rowContainer: {
        width: '95%',
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'space-between'
    },
    nameStyle: {
        flex: 1,
        height: 50,
        borderWidth: 1,
        paddingHorizontal: 8,
        borderRadius: 10,
        fontFamily: font.regular,
        borderColor: colors.borderColor
    },
    title: {
        fontSize: 20,
        width: '95%',
        marginVertical: 8,
        fontFamily: font.bold
    },
    avatarStyle: {
        height: 200,
        width: 200,
        borderRadius: 100,
        marginTop: 50
    },
    link: {
        fontSize: 20,
        fontFamily: font.regular,
        color: colors.main,
        paddingVertical: 16
    }
})

export default styles
