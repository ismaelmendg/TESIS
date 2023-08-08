%%Main code for signal analysis and machine learning model
% Developed by Ismael Mendoza
% 20/07/2022

clc; clear; close all;

M = table2array(readtable('Sujeto1_offline.csv'));

EMG_Filtro1 = Func_LPF(1, 100, 4, M,2);
EMG_Filtro2 = Func_LPF(1, 100, 4, M,3);
EMG_Filtro3 = Func_LPF(1, 100, 4, M,4);

Time = Func_Time(100);
% csvwrite('Sujeto_Features.csv', EMG_features)
EMG1_izq = Func_Gather(M, 5, 601, EMG_Filtro1, -100, 399, 25, 75);
EMG1mean_izq = Func_Average(EMG1_izq);
EMG1_std_izq = Func_std(EMG1_izq);

EMG1_der = Func_Gather(M, 5, 701, EMG_Filtro1, -100, 399, 25, 75);
EMG1mean_der = Func_Average(EMG1_der);
EMG1_std_der = Func_std(EMG1_der);

EMG1_arriba = Func_Gather(M, 5, 801, EMG_Filtro1, -100, 399, 25, 75);
EMG1mean_arriba = Func_Average(EMG1_arriba);
EMG1_std_arriba = Func_std(EMG1_arriba);

%%
EMG2_izq = Func_Gather(M, 5, 601, EMG_Filtro2, -100, 399, 25, 75);
EMG2mean_izq = Func_Average(EMG2_izq);
EMG2_std_izq = Func_std(EMG2_izq);

EMG2_der = Func_Gather(M, 5, 701, EMG_Filtro2, -100, 399, 25, 75);
EMG2mean_der = Func_Average(EMG2_der);
EMG2_std_der = Func_std(EMG2_der);

EMG2_arriba = Func_Gather(M, 5, 801, EMG_Filtro2, -100, 399, 25, 75);
EMG2mean_arriba = Func_Average(EMG2_arriba);
EMG2_std_arriba = Func_std(EMG2_arriba);
%%
EMG3_izq = Func_Gather(M, 5, 601, EMG_Filtro3, -100, 399, 25, 75);
EMG3mean_izq = Func_Average(EMG3_izq);
EMG3_std_izq = Func_std(EMG3_izq);

EMG3_der = Func_Gather(M, 5, 701, EMG_Filtro3, -100, 399, 25, 75);
EMG3mean_der = Func_Average(EMG3_der);
EMG3_std_der = Func_std(EMG3_der);

EMG3_arriba = Func_Gather(M, 5, 801, EMG_Filtro3, -100, 399, 25, 75);
EMG3mean_arriba = Func_Average(EMG3_arriba);
EMG3_std_arriba = Func_std(EMG3_arriba);
%%
EMG_izq = Func_Concatenate(EMG1_izq, EMG2_izq, EMG3_izq, 101, 400, 9);
EMG_der = Func_Concatenate(EMG1_der, EMG2_der, EMG3_der, 101, 400, 9);
EMG_arriba = Func_Concatenate(EMG1_arriba, EMG2_arriba, EMG3_arriba, 101, 400, 9);

%% Esto crea la matriz final con todas las caracteristicas y todos los intentos
EMG_features = Func_Feature(EMG_izq,EMG_der,EMG_arriba, -1, 1, 2);

[~,B] = size(EMG_features);
[idx,scores] = fscchi2(EMG_features(:,1:(B-1)),EMG_features(:,B));
figure
hold on
plot3(EMG_features(1:50,idx(1)),EMG_features(1:50,idx(2)),EMG_features(1:50,idx(3)),'o',...
    'Color','b','MarkerSize',6,...
    'MarkerFaceColor','#9999FF')

plot3(EMG_features(51:100,idx(1)),EMG_features(51:100,idx(2)),EMG_features(51:100,idx(3)),'o',...
    'Color','r','MarkerSize',6,...
    'MarkerFaceColor','#FF9999')
plot3(EMG_features(100:150,idx(1)),EMG_features(100:150,idx(2)),EMG_features(100:150,idx(3)),'o',...
    'Color','g','MarkerSize',6,...
    'MarkerFaceColor','#99FF99')
grid on
set(gca,'FontName','times','Fontsize',14)

legend('\itIzquierda\rm','\itDerecha\rm','\itArriba\rm','Location','northeast','NumColumns',2)


figure
plot(EMG_features(1:50,idx(1)),EMG_features(1:50,idx(2)),'o',...
    'Color','b','MarkerSize',6,...
    'MarkerFaceColor','#9999FF')
hold on
plot(EMG_features(51:100,idx(1)),EMG_features(51:100,idx(2)),'o',...
    'Color','r','MarkerSize',6,...
    'MarkerFaceColor','#FF9999')
plot(EMG_features(100:150,idx(1)),EMG_features(100:150,idx(2)),'o',...
    'Color','g','MarkerSize',6,...
    'MarkerFaceColor','#99FF99')
set(gca,'FontName','times','Fontsize',14)

legend('\itIzquierda\rm','\itDerecha\rm','\itArriba\rm')
xlim([-50 300])
ylim([-100 250])
%% Machine learnign classifier 
Accuracy = [];
Acc=[];
for n = 1:5
    EMG_Shuffle = Func_Shuffle(EMG_features);
    EMG_features_train = Func_FeatTrain(EMG_Shuffle);
    EMG_features_test = Func_FeatTest(EMG_Shuffle);
   
    Mdl_NB = Func_Module("fitcnb", EMG_features_train);
    Mdl_SVM = Func_Module("fitcecoc", EMG_features_train);
    Mdl_DT = Func_Module("fitctree", EMG_features_train);
    Mdl_KNN = Func_Module("fitcknn", EMG_features_train);
    Mdl_QDA = Func_Module("fitcdiscrq", EMG_features_train);
    Mdl_LDA = Func_Module("fitcdiscr", EMG_features_train);
    
    [A, B] = size(EMG_features_test);
    
    EMG_NB = Func_Predict(Mdl_NB, EMG_features_test);
    EMG_SVM = Func_Predict(Mdl_SVM, EMG_features_test);
    EMG_DT = Func_Predict(Mdl_DT, EMG_features_test);
    EMG_KNN = Func_Predict(Mdl_KNN, EMG_features_test);
    EMG_QDA = Func_Predict(Mdl_QDA, EMG_features_test);
    EMG_LDA = Func_Predict(Mdl_LDA, EMG_features_test);
    
    Accuracy = Func_Accuracy(Accuracy,n,EMG_features_test, EMG_NB, EMG_SVM, EMG_DT, EMG_KNN, EMG_QDA, EMG_LDA);

end
% close all
Models = {'NB';'SVM';'DT';'KNN';'QDA';'LDA'};
Accuracy = mean(Accuracy,2);
Table= table(Models,Accuracy)
Accuray = mean(Accuracy,1)
%%
x2 = [Time; flipud(Time)];
figure
subplot(331)
inBetween = [EMG1mean_izq - EMG1_std_izq; flipud(EMG1mean_izq + EMG1_std_izq)];
fill(x2, inBetween, 'b');
alpha(.4)
hold on
title('Pectoral')
%plot(Time,EMG1_izq, 'color' , [0.7529 0.7529 0.7529])
plot(Time, EMG1mean_izq,'b', 'LineWidth',1.5)
plot(Time, EMG1mean_izq + EMG1_std_izq,'b', 'LineWidth',1.5)
plot(Time, EMG1mean_izq - EMG1_std_izq,'b', 'LineWidth',1.5)
%set(gca,'FontName','times','Fontsize',14)
ft = 'Times'; 
set(gca, 'FontName', ft,'Fontsize',14)
%xlabel('\itTiempo (seg)\rm');
ylabel('\itIzquierda\rm');
hold off
xline(0, '--','Inicio', 'FontName', ft,'Fontsize',14, 'LineWidth',2)
xline(3, '--', 'Fin','Fontsize',14, 'LineWidth',2)
ylim([0 300])
xlim([-1 4])


subplot(334)
inBetween = [EMG1mean_der - EMG1_std_der; flipud(EMG1mean_der + EMG1_std_der)];
fill(x2, inBetween, 'r');
alpha(.4)
hold on
%plot(Time,EMG1_der,'color' , [0.7529 0.7529 0.7529])
plot(Time, EMG1mean_der,'r', 'LineWidth',1.5)
plot(Time, EMG1mean_der + EMG1_std_der,'r', 'LineWidth',1.5)
plot(Time, EMG1mean_der - EMG1_std_der,'r', 'LineWidth',1.5)
ft = 'Times'; 
set(gca, 'FontName', ft,'Fontsize',14)
%xlabel('\itTiempo (seg)\rm');
ylabel('\itDerecha\rm');
hold off
xline(0, '--', 'Inicio','Fontsize',14, 'LineWidth',2)
xline(3, '--', 'Fin','Fontsize',14, 'LineWidth',2)
ylim([0 300])
xlim([-1 4])

subplot(337)
inBetween = [EMG1mean_arriba - EMG1_std_arriba; flipud(EMG1mean_arriba + EMG1_std_arriba)];
fill(x2, inBetween, 'g');
alpha(.4)
hold on
%plot(Time,EMG1_arriba,'color' , [0.5 0.5 0.5])
ft = 'Times'; 
set(gca, 'FontName', ft,'Fontsize',14)
plot(Time, EMG1mean_arriba,'g', 'LineWidth',1.5)
plot(Time, EMG1mean_arriba + EMG1_std_arriba,'g', 'LineWidth',1.5)
plot(Time, EMG1mean_arriba - EMG1_std_arriba,'g', 'LineWidth',1.5)
ft = 'Times'; 
set(gca, 'FontName', ft,'Fontsize',14)
xlabel('\itTiempo (seg)\rm');
ylabel('\itArriba\rm');
hold off
xline(0, '--', 'Inicio','Fontsize',14, 'LineWidth',2)
xline(3, '--', 'Fin','Fontsize',14, 'LineWidth',2)
ylim([0 300])
xlim([-1 4])

subplot(332)
inBetween = [EMG2mean_izq - EMG2_std_izq; flipud(EMG2mean_izq + EMG2_std_izq)];
fill(x2, inBetween, 'b');
alpha(.4)
hold on
title('Trapecio')
%plot(Time,EMG2_izq,'color' , [0.5 0.5 0.5])
plot(Time, EMG2mean_izq,'b', 'LineWidth',1.5)
plot(Time, EMG2mean_izq + EMG2_std_izq,'b', 'LineWidth',1.5)
plot(Time, EMG2mean_izq - EMG2_std_izq,'b', 'LineWidth',1.5)
ft = 'Times'; 
set(gca, 'FontName', ft,'Fontsize',14)
%xlabel('\itTiempo (seg)\rm');
%ylabel('\itArriba\rm');
hold off
xline(0, '--', 'Inicio','Fontsize',14, 'LineWidth',2)
xline(3, '--', 'Fin','Fontsize',14, 'LineWidth',2)
ylim([0 300])
xlim([-1 4])

subplot(335)
inBetween = [EMG2mean_der - EMG2_std_der; flipud(EMG2mean_der + EMG2_std_der)];
fill(x2, inBetween, 'r');
alpha(.4)
hold on
%plot(Time,EMG2_der,'color' , [0.5 0.5 0.5])
plot(Time, EMG2mean_der,'r', 'LineWidth',1.5)
plot(Time, EMG2mean_der + EMG2_std_der,'r', 'LineWidth',1.5)
plot(Time, EMG2mean_der - EMG2_std_der,'r', 'LineWidth',1.5)
ft = 'Times'; 
set(gca, 'FontName', ft,'Fontsize',14)
%xlabel('\itTiempo (seg)\rm');
%ylabel('\itArriba\rm');
hold off
xline(0, '--', 'Inicio','Fontsize',14, 'LineWidth',2)
xline(3, '--', 'Fin','Fontsize',14, 'LineWidth',2)
ylim([0 300])
xlim([-1 4])

subplot(338)
inBetween = [EMG2mean_arriba - EMG2_std_arriba; flipud(EMG2mean_arriba + EMG2_std_arriba)];
fill(x2, inBetween, 'g');
alpha(.4)
hold on
%plot(Time,EMG2_arriba,'color' , [0.5 0.5 0.5])
plot(Time, EMG2mean_arriba,'g', 'LineWidth',1.5)
plot(Time, EMG2mean_arriba + EMG2_std_arriba,'g', 'LineWidth',1.5)
plot(Time, EMG2mean_arriba - EMG2_std_arriba,'g', 'LineWidth',1.5)
ft = 'Times'; 
set(gca, 'FontName', ft,'Fontsize',14)
xlabel('\itTiempo (seg)\rm');
%ylabel('\itArriba\rm');
hold off
xline(0, '--', 'Inicio','Fontsize',14, 'LineWidth',2)
xline(3, '--', 'Fin','Fontsize',14, 'LineWidth',2)
ylim([0 300])
xlim([-1 4])

subplot(333)
inBetween = [EMG3mean_izq - EMG3_std_izq; flipud(EMG3mean_izq + EMG3_std_izq)];
fill(x2, inBetween, 'b');
alpha(.4)
hold on
title('Dorsal')
%plot(Time,EMG3_izq,'color' , [0.5 0.5 0.5])
plot(Time, EMG3mean_izq,'b', 'LineWidth',1.5)
plot(Time, EMG3mean_izq + EMG3_std_izq,'b', 'LineWidth',1.5)
plot(Time, EMG3mean_izq - EMG3_std_izq,'b', 'LineWidth',1.5)
ft = 'Times'; 
set(gca, 'FontName', ft,'Fontsize',14)
%xlabel('\itTiempo (seg)\rm');
%ylabel('\itArriba\rm');
hold off
xline(0, '--', 'Inicio','Fontsize',14, 'LineWidth',2)
xline(3, '--', 'Fin','Fontsize',14, 'LineWidth',2)
ylim([0 300])
xlim([-1 4])

subplot(336)
inBetween = [EMG3mean_der - EMG3_std_der; flipud(EMG3mean_der + EMG3_std_der)];
fill(x2, inBetween, 'r');
alpha(.4)
hold on
%plot(Time,EMG3_der,'color' , [0.5 0.5 0.5])
plot(Time, EMG3mean_der,'r', 'LineWidth',1.5)
plot(Time, EMG3mean_der + EMG3_std_der,'r', 'LineWidth',1.5)
plot(Time, EMG3mean_der - EMG3_std_der,'r', 'LineWidth',1.5)
ft = 'Times'; 
set(gca, 'FontName', ft,'Fontsize',14)
%xlabel('\itTiempo (seg)\rm');
%ylabel('\itArriba\rm');
hold off
xline(0, '--', 'Inicio','Fontsize',14, 'LineWidth',2)
xline(3, '--', 'Fin','Fontsize',14, 'LineWidth',2)
ylim([0 300])
xlim([-1 4])

subplot(339)
inBetween = [EMG3mean_arriba - EMG3_std_arriba; flipud(EMG3mean_arriba + EMG3_std_arriba)];
fill(x2, inBetween, 'g');
alpha(.4)
hold on
%plot(Time,EMG3_arriba,'color' , [0.5 0.5 0.5])
plot(Time, EMG3mean_arriba,'g', 'LineWidth',1.5)
plot(Time, EMG3mean_arriba + EMG3_std_arriba,'g', 'LineWidth',1.5)
plot(Time, EMG3mean_arriba - EMG3_std_arriba,'g', 'LineWidth',1.5)
ft = 'Times'; 
set(gca, 'FontName', ft,'Fontsize',14)
xlabel('\itTiempo (seg)\rm');
%ylabel('\itArriba\rm');
hold off
xline(0, '--', 'Inicio','Fontsize',14, 'LineWidth',2)
xline(3, '--', 'Fin','Fontsize',14, 'LineWidth',2)
ylim([0 300])
xlim([-1 4])
%%
close all

EMG_1 = M(:,2);
EMG_2 = M(:,3);
EMG_3 = M(:,4);
trigger =  M(:,5);

T = 1/100;
 DataOut = (0:(1/100):1196.60)';
t = 3.3/1024; 
figure
subplot(311)
hold on
plot(DataOut, EMG_1*t, 'color', '[0.7529 0.7529 0.7529]') 
plot(DataOut, EMG_Filtro1*t,'linewidth',2, 'color', '[0.8500 0.3250 0.0980]')
title('unfiltered and filtered signal of EMG_1 ')
xlabel('Time (s)')
ylabel('Amplitude (V)')
xlim([0 50])
ylim([0 1])

subplot(312)
hold on
plot(DataOut,EMG_2*t-.18, 'color', '[0.7529 0.7529 0.7529]')  
plot(DataOut,EMG_Filtro2*t-.18,'linewidth',2,'color', '[0.8500 0.3250 0.0980]')
title('unfiltered and filtered signal of EMG_2 ')
xlabel('Time (s)')
ylabel('Amplitude (V)')
xlim([0 50])
ylim([0 1])

subplot(313)
hold on
plot(DataOut,EMG_3*t-.1, 'color', '[0.7529 0.7529 0.7529]')
plot(DataOut,EMG_Filtro3*t-.1,'linewidth',2,'color', '[0.8500 0.3250 0.0980]')  
title('unfiltered and filtered signal of EMG_3 ')
xlabel('Time (s)')
ylabel('Amplitude (V)')
xlim([0 50])
ylim([0 1])
%%
hold on
plot(DataOut,EMG_2*t-.166, 'color', '[0.8500 0.3250 0.0980]')
title('Surround EMG signal')
ylabel('Amplitude (V)');
xlabel('Time (s)');
xlim([0 33])
ylim([0 1])

%%
close all
hold on
plot(DataOut,trigger,'linewidth',2, 'color', '[0.8500 0.3250 0.0980]')
title('Trigger')
ylabel('Value');
xlabel('Time (s)');
xlim([150.3 173.5])
ylim([0 1100])
%%
% figure
% subplot(311)
% plot(TimeCon,EMG_izq)
% ylim([0 400])
% title('EMG IZQUIERDA')
% xlabel('Time (sec)','FontSize',9);
% subplot(312)
% plot(TimeCon,EMG_der)
% ylim([0 400])
% title('EMG DERECHA')
% xlabel('Time (sec)','FontSize',9);
% subplot(313)
% plot(TimeCon,EMG_arriba)
% ylim([0 400])
% title('EMG ARRIBA')
% xlabel('Time (sec)','FontSize',9);
% figure
% cm = confusionchart(EMG_features_test(:,28),EMG_SVM);
%%
% figure
% subplot(331)
% inBetween = [EMG1mean_izqNor - EMG1_std_izqNor; flipud(EMG1mean_izqNor + EMG1_std_izqNor)];
% fill(x2, inBetween, 'r');
% alpha(.2)
% hold on
% plot(Time,EMG1_izqNor,'color' , [0.5 0.5 0.5])
% plot(Time, EMG1mean_izqNor,'-.r', 'LineWidth',1.5)
% plot(Time, EMG1mean_izqNor + EMG1_std_izqNor,':r', 'LineWidth',1.5)
% plot(Time, EMG1mean_izqNor - EMG1_std_izqNor,':r', 'LineWidth',1.5)
% ylim([0 1])
% xline(0, 'LineWidth',2)
% xline(3, 'LineWidth',2)
% xlabel('Time (sec)','FontSize',9);
% title('EMG_1NOR')
% hold off
% subplot(334)
% inBetween = [EMG1mean_derNor - EMG1_std_derNor; flipud(EMG1mean_derNor + EMG1_std_derNor)];
% fill(x2, inBetween, 'r');
% alpha(.2)
% hold on
% plot(Time,EMG1_derNor,'color' , [0.5 0.5 0.5])
% plot(Time, EMG1mean_derNor,'-.r', 'LineWidth',1.5)
% plot(Time, EMG1mean_derNor + EMG1_std_derNor,':r', 'LineWidth',1.5)
% plot(Time, EMG1mean_derNor - EMG1_std_derNor,':r', 'LineWidth',1.5)
% ylim([0 1])
% xline(0, 'LineWidth',2)
% xline(3, 'LineWidth',2)
% xlabel('Time (sec)','FontSize',9);
% hold off
% subplot(337)
% inBetween = [EMG1mean_arribaNor - EMG1_std_arribaNor; flipud(EMG1mean_arribaNor + EMG1_std_arribaNor)];
% fill(x2, inBetween, 'r');
% alpha(.2)
% hold on
% plot(Time,EMG1_arribaNor,'color' , [0.5 0.5 0.5])
% plot(Time, EMG1mean_arribaNor,'-.r', 'LineWidth',1.5)
% plot(Time, EMG1mean_arribaNor + EMG1_std_arribaNor,':r', 'LineWidth',1.5)
% plot(Time, EMG1mean_arribaNor - EMG1_std_arribaNor,':r', 'LineWidth',1.5)
% ylim([0 1])
% xline(0, 'LineWidth',2)
% xline(3, 'LineWidth',2)
% xlabel('Time (sec)','FontSize',9);
% hold off
% subplot(332)
% inBetween = [EMG2mean_izqNor - EMG2_std_izqNor; flipud(EMG2mean_izqNor + EMG2_std_izqNor)];
% fill(x2, inBetween, 'r');
% alpha(.2)
% hold on
% plot(Time,EMG2_izqNor,'color' , [0.5 0.5 0.5])
% plot(Time, EMG2mean_izqNor,'-.r', 'LineWidth',1.5)
% plot(Time, EMG2mean_izqNor + EMG2_std_izqNor,':r', 'LineWidth',1.5)
% plot(Time, EMG2mean_izqNor - EMG2_std_izqNor,':r', 'LineWidth',1.5)
% ylim([0 1])
% xline(0, 'LineWidth',2)
% xline(3, 'LineWidth',2)
% xlabel('Time (sec)','FontSize',9);
% title('EMG_2NOR')
% hold off
% subplot(335)
% inBetween = [EMG2mean_derNor - EMG2_std_derNor; flipud(EMG2mean_derNor + EMG2_std_derNor)];
% fill(x2, inBetween, 'r');
% alpha(.2)
% hold on
% plot(Time,EMG2_derNor,'color' , [0.5 0.5 0.5])
% plot(Time, EMG2mean_derNor,'-.r', 'LineWidth',1.5)
% plot(Time, EMG2mean_derNor + EMG2_std_derNor,':r', 'LineWidth',1.5)
% plot(Time, EMG2mean_derNor - EMG2_std_derNor,':r', 'LineWidth',1.5)
% ylim([0 1])
% xline(0, 'LineWidth',2)
% xline(3, 'LineWidth',2)
% xlabel('Time (sec)','FontSize',9);
% hold off
% subplot(338)
% inBetween = [EMG2mean_arribaNor - EMG2_std_arribaNor; flipud(EMG2mean_arribaNor + EMG2_std_arribaNor)];
% fill(x2, inBetween, 'r');
% alpha(.2)
% hold on
% plot(Time,EMG2_arribaNor,'color' , [0.5 0.5 0.5])
% plot(Time, EMG2mean_arribaNor,'-.r', 'LineWidth',1.5)
% plot(Time, EMG2mean_arribaNor + EMG2_std_arribaNor,':r', 'LineWidth',1.5)
% plot(Time, EMG2mean_arribaNor - EMG2_std_arribaNor,':r', 'LineWidth',1.5)
% ylim([0 1])
% xline(0, 'LineWidth',2)
% xline(3, 'LineWidth',2)
% xlabel('Time (sec)','FontSize',9);
% hold off
% subplot(333)
% inBetween = [EMG3mean_izqNor - EMG3_std_izqNor; flipud(EMG3mean_izqNor + EMG3_std_izqNor)];
% fill(x2, inBetween, 'r');
% alpha(.2)
% hold on
% plot(Time,EMG3_izqNor,'color' , [0.5 0.5 0.5])
% plot(Time, EMG3mean_izqNor,'-.r', 'LineWidth',1.5)
% plot(Time, EMG3mean_izqNor + EMG3_std_izqNor,':r', 'LineWidth',1.5)
% plot(Time, EMG3mean_izqNor - EMG3_std_izqNor,':r', 'LineWidth',1.5)
% ylim([0 1])
% xline(0, 'LineWidth',2)
% xline(3, 'LineWidth',2)
% xlabel('Time (sec)','FontSize',9);
% title('EMG_3NOR')
% hold off
% subplot(336)
% inBetween = [EMG3mean_derNor - EMG3_std_derNor; flipud(EMG3mean_derNor + EMG3_std_derNor)];
% fill(x2, inBetween, 'r');
% alpha(.2)
% hold on
% plot(Time,EMG3_derNor,'color' , [0.5 0.5 0.5])
% plot(Time, EMG3mean_derNor,'-.r', 'LineWidth',1.5)
% plot(Time, EMG3mean_derNor + EMG3_std_derNor,':r', 'LineWidth',1.5)
% plot(Time, EMG3mean_derNor - EMG3_std_derNor,':r', 'LineWidth',1.5)
% ylim([0 1])
% xline(0, 'LineWidth',2)
% xline(3, 'LineWidth',2)
% xlabel('Time (sec)','FontSize',9);
% hold off
% subplot(339)
% inBetween = [EMG3mean_arribaNor - EMG3_std_arribaNor; flipud(EMG3mean_arribaNor + EMG3_std_arribaNor)];
% fill(x2, inBetween, 'r');
% alpha(.2)
% hold on
% plot(Time,EMG3_arribaNor,'color' , [0.5 0.5 0.5])
% plot(Time, EMG3mean_arribaNor,'-.r', 'LineWidth',1.5)
% plot(Time, EMG3mean_arribaNor + EMG3_std_arribaNor,':r', 'LineWidth',1.5)
% plot(Time, EMG3mean_arribaNor - EMG3_std_arribaNor,':r', 'LineWidth',1.5)
% ylim([0 1])
% xline(0, 'LineWidth',2)
% xline(3, 'LineWidth',2)
% xlabel('Time (sec)','FontSize',9);
% hold off
% %%
% figure
% subplot(3,1,1)
% plot(Time, EMG1mean_izq, Time, EMG1mean_der, Time, EMG1mean_arriba)
% ylim([0 350])
% title('EMG_1')
% xlabel('Time (sec)','FontSize',9);
% legend('Izquierdo','Derecho','Arriba');
% 
% subplot(3,1,2)
% plot(Time, EMG2mean_izq, Time, EMG2mean_der, Time, EMG2mean_arriba)
% ylim([0 350])
% title('EMG_2')
% xlabel('Time (sec)','FontSize',9);
% legend('Izquierdo','Derecho','Arriba');
% 
% subplot(3,1,3)
% plot(Time, EMG3mean_izq, Time, EMG3mean_der, Time, EMG3mean_arriba)
% ylim([0 350])
% title('EMG_3')
% xlabel('Time (sec)','FontSize',9);
% legend('Izquierdo','Derecho','Arriba');
% %%
% figure
% subplot(3,1,1)
% plot(Time, EMG1mean_izqNor, Time, EMG1mean_derNor, Time, EMG1mean_arribaNor)
% ylim([0 1])
% title('xxxEMG_1NOR')
% xlabel('Time (sec)','FontSize',9);
% legend('Izquierdo','Derecho','Arriba');
%  
% subplot(3,1,2)
% plot(Time, EMG2mean_izqNor, Time, EMG2mean_derNor, Time, EMG2mean_arribaNor)
% ylim([0 1])
% title('EMG_2NOR')
% xlabel('Time (sec)','FontSize',9);
% legend('Izquierdo','Derecho','Arriba');
% 
% subplot(3,1,3)
% plot(Time, EMG3mean_izqNor, Time, EMG3mean_derNor, Time, EMG3mean_arribaNor)
% ylim([0 1])
% title('EMG_3NOR')
% xlabel('Time (sec)','FontSize',9);
% legend('Izquierdo','Derecho','Arriba');
