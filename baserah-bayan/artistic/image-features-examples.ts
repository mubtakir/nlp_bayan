import { ImageCommonFeaturesExtractor } from "./image-common-features-extractor";

export class ImageFeaturesExamples {
  static processImage(imageData: ImageData): void {
    const extractor = new ImageCommonFeaturesExtractor();
    extractor.loadImage(imageData);
    const features = extractor.extractAll();
  }
}
