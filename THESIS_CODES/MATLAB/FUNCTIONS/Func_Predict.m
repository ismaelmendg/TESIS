%%PREDICTION FUNCTION WITH MACHINE LEARNING MODEL
%DModel - Model to use
%FeatTest - Values to predict
% Developed by Ismael Mendoza
% 20/07/2022
function DataOut = Func_Predict(DModel, FeatTest)
    
    [~, B] = size(FeatTest);
    DataOut = predict(DModel,FeatTest(:,1:B-1));

end