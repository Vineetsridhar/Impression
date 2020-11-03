//Returns height and width
import { Dimensions, PixelRatio } from 'react-native';

const { height, width } = Dimensions.get("window");

const metrics = {
    DEVICE_WIDTH: width,
    DEVICE_HEIGHT: height,
    HEIGHT_PIXELS: PixelRatio.getPixelSizeForLayoutSize(height),
    WIDTH_PIXELS: PixelRatio.getPixelSizeForLayoutSize(width)
}

export default metrics;