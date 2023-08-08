%%FEATURE FUNCTION TRAIN
%DataIn - percentage of data for feature train
% Developed by Ismael Mendoza
% 20/07/2022

function DataOut = Func_FeatTrain(DataIn)

    DataOut = DataIn(1:length(DataIn)*.8,:);

end