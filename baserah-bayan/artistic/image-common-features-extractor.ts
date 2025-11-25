export interface ImageFeatures {
  edges: number[][];
  corners: Array<{x: number; y: number}>;
  contours: Array<Array<{x: number; y: number}>>;
  colors: Array<{r: number; g: number; b: number; frequency: number}>;
}

export class ImageCommonFeaturesExtractor {
  imageData: ImageData | null;
  features: ImageFeatures;

  constructor() {
    this.imageData = null;
    this.features = {
      edges: [],
      corners: [],
      contours: [],
      colors: []
    };
  }

  loadImage(imageData: ImageData): void {
    this.imageData = imageData;
  }

  extractEdges(): number[][] {
    if (!this.imageData) return [];
    return [];
  }

  extractCorners(): Array<{x: number; y: number}> {
    return [];
  }

  extractContours(): Array<Array<{x: number; y: number}>> {
    return [];
  }

  extractColors(): Array<{r: number; g: number; b: number; frequency: number}> {
    return [];
  }

  extractAll(): ImageFeatures {
    this.features.edges = this.extractEdges();
    this.features.corners = this.extractCorners();
    this.features.contours = this.extractContours();
    this.features.colors = this.extractColors();
    return this.features;
  }
}
